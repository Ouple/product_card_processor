from pathlib import Path
import time

from app.image_io import load_image, save_image, get_image_paths

from app.transforms import (resize_to_fit,
                            paste_centered,
                            calculate_scaled_fit_area,
                            create_blank_canvas)
from app.background_removal import remove_background, create_background_removal_session

import json

class ImageProcessor:

    def __init__(self, input_folder, output_folder,
                 canvas_width, canvas_height,
                 allow_upscale=True, template_path=None,
                 offset_x=0, offset_y=0, product_scale=0.8,
                 remove_bg=False, bg_backend="rembg", bg_session=None, bg_model="u2net"):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.max_image_width = None
        self.max_image_height = None
        self.allow_upscale = allow_upscale
        self.template_path = template_path
        self.processed_count = 0
        self.failed_count = 0
        self.failed_files = []
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.product_scale = product_scale
        self.remove_bg = remove_bg
        self.bg_backend = bg_backend
        self.bg_session = bg_session
        self.bg_model = bg_model
        self.processing_time_seconds = None

    def get_settings(self):
        return {"input_folder": str(self.input_folder),
                "output_folder": str(self.output_folder),
                "canvas_width": self.canvas_width,
                "canvas_height": self.canvas_height,
                "allow_upscale": self.allow_upscale,
                "template_path": str(self.template_path) if self.template_path else None,
                "offset_x": self.offset_x,
                "offset_y": self.offset_y,
                "product_scale": self.product_scale,
                "remove_bg": self.remove_bg,
                "bg_backend": self.bg_backend,
                "bg_model": self.bg_model
                }

    def get_report(self):
        return {
            "processed_count": self.processed_count,
            "failed_count": self.failed_count,
            "failed_files": self.failed_files,
            "settings": self.get_settings(),
            "processing_time_seconds": round(self.processing_time_seconds,3) if self.processing_time_seconds else None
        }
    def save_report(self, report_path):
        report = self.get_report()
        report_path = Path(report_path)
        report_path.parent.mkdir(parents=True, exist_ok=True)

        with open(report_path, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4, ensure_ascii=False)

    def process_single_image(self, image_path):
        image = load_image(image_path)

        if self.remove_bg:
            image = remove_background(image, backend=self.bg_backend, session=self.bg_session)

        if self.template_path:
            background = load_image(self.template_path)
        else:
            background = create_blank_canvas(self.canvas_width, self.canvas_height)

        base_width, base_height = background.size

        target_width, target_height = calculate_scaled_fit_area(base_width,
                                                                base_height,
                                                                self.product_scale
                                                                )
        resized_image = resize_to_fit(image,
                                      target_width,
                                      target_height,
                                      allow_upscale=self.allow_upscale
                                      )
        canvas = paste_centered(background,
                                resized_image,
                                offset_x=self.offset_x,
                                offset_y=self.offset_y
                                )

        output_path = self.output_folder / image_path.name
        save_image(canvas, output_path)
        self.processed_count += 1

        return output_path

    def process_all_images(self):
        if not self.input_folder.exists():
            raise FileNotFoundError(f"Input folder does not exist: {self.input_folder}")

        if not self.input_folder.is_dir():
            raise NotADirectoryError(f"Input folder is not a directory: {self.input_folder}")

        self.output_folder.mkdir(parents=True, exist_ok=True)

        image_paths = get_image_paths(self.input_folder)

        if not image_paths:
            raise ValueError(f"No images found in input folder: {self.input_folder}")
        start_time = time.perf_counter()
        if self.remove_bg:
            self.bg_session = create_background_removal_session(backend=self.bg_backend,
                                                                model_name=self.bg_model,
                                                                )
        for image_path in image_paths:
            try:
                output_path = self.process_single_image(image_path)
                end_time = time.perf_counter()
                self.processing_time_seconds = end_time - start_time
                print(output_path)
            except OSError as error:
                print(f"File was not processed: {image_path}\nReason: {error}")
                self.failed_count += 1
                self.failed_files.append({
                    "image_path": str(image_path),
                    "reason": str(error)
                })

        return self.processed_count


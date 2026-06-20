from app.image_io import load_image, save_image, get_image_paths

from app.transforms import resize_to_fit, create_centered_canvas


class ImageProcessor:

    def __init__(self, input_folder, output_folder,
                 canvas_width, canvas_height,
                 max_image_width, max_image_height, allow_upscale=True):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.max_image_width = max_image_width
        self.max_image_height = max_image_height
        self.allow_upscale = allow_upscale
        self.processed_count = 0
        self.failed_count = 0

    def get_settings(self):
        return {"input_folder": self.input_folder,
                "output_folder": self.output_folder,
                "canvas_width": self.canvas_width,
                "canvas_height": self.canvas_height,
                "max_image_width": self.max_image_width,
                "max_image_height": self.max_image_height,
                "allow_upscale": self.allow_upscale
                }

    def process_single_image(self, image_path):
        image = load_image(image_path)
        resized_image = resize_to_fit(image,
                                      self.max_image_width,
                                      self.max_image_height,
                                      allow_upscale=self.allow_upscale
                                      )
        canvas = create_centered_canvas(resized_image, self.canvas_width, self.canvas_height)

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

        for image_path in image_paths:
            try:
                output_path = self.process_single_image(image_path)
                print(output_path)
            except OSError as error:
                print(f"File was not processed: {image_path}\nReason: {error}")
                self.failed_count += 1

        return self.processed_count


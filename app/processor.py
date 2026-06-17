from app.image_io import load_image, save_image, get_image_paths

from app.transforms import resize_to_fit, create_centered_canvas


class ImageProcessor:

    def __init__(self, input_folder, output_folder,
                 canvas_width, canvas_height,
                 max_image_width, max_image_height):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.max_image_width = max_image_width
        self.max_image_height = max_image_height
        self.processed_count = 0

    def get_settings(self):
        return {"input_folder": self.input_folder,
                "output_folder": self.output_folder,
                "canvas_width": self.canvas_width,
                "canvas_height": self.canvas_height,
                "max_image_width": self.max_image_width,
                "max_image_height": self.max_image_height
        }

    def process_single_image(self, image_path):
        image = load_image(image_path)
        resized_image = resize_to_fit(image, self.max_image_width, self.max_image_height)
        canvas = create_centered_canvas(resized_image, self.canvas_width, self.canvas_height)

        output_path = self.output_folder / image_path.name
        save_image(canvas, output_path)
        self.processed_count += 1

        return output_path

    def process_all_images(self):
        image_paths = get_image_paths(self.input_folder)
        for image_path in image_paths:
            output_path = self.process_single_image(image_path)
            print(output_path)

        return self.processed_count


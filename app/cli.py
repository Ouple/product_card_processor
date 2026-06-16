from app.image_io import load_image, save_image
from app.image_io import get_image_paths
from app.transforms import resize_to_fit
from app.transforms import create_centered_canvas

from pathlib import Path


canvas_width = 1080
canvas_height = 1440
max_width = 900
max_height = 1200

image_paths = get_image_paths("data/input")

output_folder = Path("data/output")

for item in image_paths:
    image = load_image(item)
    original_width, original_height = image.size
    resized_image = resize_to_fit(image, max_width, max_height)
    canvas = create_centered_canvas(resized_image, canvas_width, canvas_height)

    output_path = output_folder / item.name
    save_image(canvas, output_path)
    print(f"image saved to {output_path}")



from app.image_io import load_image, save_image
from app.image_io import get_image_paths
from pathlib import Path

image_paths = get_image_paths("data/input")

output_folder = Path("data/output")

for item in image_paths:
    image = load_image(item)
    output_path = output_folder / item.name
    save_image(image, output_path)
    print(f"Image saved to: {output_path}")


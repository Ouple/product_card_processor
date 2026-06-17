from app.image_io import load_image, save_image
from app.image_io import get_image_paths

from app.transforms import resize_to_fit
from app.transforms import create_centered_canvas

from app.config import INPUT_FOLDER, OUTPUT_FOLDER, CANVAS_WIDTH, CANVAS_HEIGHT, MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT

image_paths = get_image_paths(INPUT_FOLDER)


for item in image_paths:
    image = load_image(item)
    resized_image = resize_to_fit(image, MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT)
    canvas = create_centered_canvas(resized_image, CANVAS_WIDTH, CANVAS_HEIGHT)

    output_path = OUTPUT_FOLDER / item.name
    save_image(canvas, output_path)
    print(f"image saved to {output_path}")



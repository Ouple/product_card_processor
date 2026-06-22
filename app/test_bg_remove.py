from PIL import Image
from app.image_io import save_image
from pathlib import Path

image = Image.open("data/input/test.JPG")


def rembg_remover(image):
    path = Path("data/output/test_2.png")
    from rembg import remove
    output_image = remove(image)
    save_image(output_image, path)
    return print("OK")


rembg_remover(image)
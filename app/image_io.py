import os

from PIL import Image
from pathlib import Path

def load_image(path):
    return Image.open(path)

def save_image(image, path):
    image.save(path)

def get_image_paths(input_folder):
    p = Path(input_folder)
    file_list = []

    for item in p.iterdir():
        if item.is_file() and item.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]:
            file_list.append(item)
    return file_list



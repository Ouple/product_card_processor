from PIL import Image
from pathlib import Path


def make_gif(before_path, after_path, output_path):
    before_path = Path(before_path)
    after_path = Path(after_path)
    output_path = Path(output_path)

    before_image = Image.open(before_path)
    after_image = Image.open(after_path)

    if before_image.size != after_image.size:
        after_image = after_image.resize(before_image.size)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    before_image.save(
        output_path,
        save_all=True,
        append_images=[after_image],
        duration=1200,
        loop=0
    )


make_gif(
    "docs/assets/demo_frames/before.jpg",
    "docs/assets/demo_frames/after.jpg",
    "docs/assets/demo_frames/demo.gif"
)
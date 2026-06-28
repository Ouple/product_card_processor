from pathlib import Path
from PIL import Image, ImageOps


def fit_to_canvas(image, canvas_size, background_color="white"):
    image = image.convert("RGB")

    fitted_image = ImageOps.contain(
        image,
        canvas_size,
        method=Image.Resampling.LANCZOS
    )

    canvas = Image.new("RGB", canvas_size, background_color)

    x = (canvas.width - fitted_image.width) // 2
    y = (canvas.height - fitted_image.height) // 2

    canvas.paste(fitted_image, (x, y))

    return canvas


def make_gif(before_path, after_path, output_path):
    before_path = Path(before_path)
    after_path = Path(after_path)
    output_path = Path(output_path)

    before_image = Image.open(before_path)
    after_image = Image.open(after_path)

    canvas_size = after_image.size

    before_frame = fit_to_canvas(before_image, canvas_size)
    after_frame = fit_to_canvas(after_image, canvas_size)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    before_frame.save(
        output_path,
        save_all=True,
        append_images=[after_frame],
        duration=1200,
        loop=0,
        optimize=True,
    )


make_gif(
    "docs/assets/demo_frames/before.jpg",
    "docs/assets/demo_frames/after.jpg",
    "docs/assets/demo_frames/demo_1.gif"
)
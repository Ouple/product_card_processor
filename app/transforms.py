from PIL import Image

def calculate_fit_size(original_width, original_height, max_width, max_height, allow_upscale=True):
    scale_by_width = max_width / original_width
    scale_by_height = max_height / original_height
    scale = min(scale_by_width, scale_by_height)
    if not allow_upscale:
        scale = min(scale, 1)
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)
    return new_width, new_height


def resize_to_fit(image, max_width, max_height, allow_upscale=True):
    original_width, original_height = image.size
    new_width, new_height = calculate_fit_size(
        original_width,
        original_height,
        max_width,
        max_height,
        allow_upscale=allow_upscale)
    return image.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)


def create_blank_canvas(width, height, color="white"):
    canvas = Image.new(mode="RGB", size=(width, height), color=color)
    return canvas


def paste_centered(background, image, offset_x=0, offset_y=0):
    image_width, image_height = image.size
    canvas_width, canvas_height = background.size
    x = ((canvas_width - image_width) // 2) + offset_x
    y = ((canvas_height - image_height) // 2) + offset_y
    canvas = background.copy()
    canvas.paste(image, (x, y))
    return canvas


def create_centered_canvas(image, canvas_width, canvas_height, color="white", offset_x=0, offset_y=0):
    canvas = create_blank_canvas(canvas_width, canvas_height, color)
    return paste_centered(canvas,
                          image,
                          offset_x=offset_x,
                          offset_y=offset_y
                          )






SUPPORTED_BACKENDS = ["rembg", "bria_rmbg"]

def remove_background(image, backend="rembg"):
    if backend == "rembg":
        return rembg_remover(image)
    elif backend == "bria_rmbg":
        raise NotImplementedError("This backend is not supported yet")
    else:
        raise ValueError(f"Unsupported background removal backend: {backend}")


def rembg_remover(image):
    from rembg import remove
    output_image = remove(image)
    return output_image


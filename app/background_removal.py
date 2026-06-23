


SUPPORTED_BACKENDS = ["rembg"]

def remove_background(image, backend="rembg", session=None):
    if backend == "rembg":
        return rembg_remover(image, session=session)
    elif backend == "bria_rmbg":
        raise NotImplementedError("This backend is not supported yet")
    else:
        raise ValueError(f"Unsupported background removal backend: {backend}")


def rembg_remover(image, session=None):
    if session is not None:
        from rembg import remove
        return remove(image, session=session)
    else:
        return remove(image)


def create_background_removal_session(backend="rembg", model_name="u2net"):
    from rembg import new_session
    if backend == "rembg":
        session = new_session(model_name)
    else:
        raise ValueError(f"Unsupported background removal backend: {backend}")
    return session
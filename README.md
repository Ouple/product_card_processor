# Product Card Processor

A Python CLI tool for preparing product images for marketplace cards.

## Current version

v0.11 — background removal with rembg backend

## Features

* Processes all supported images from an input folder
* Supports batch image processing
* Resizes product images relative to the canvas or template size
* Places product images on a configurable canvas or custom template
* Supports custom template/background images
* Uses the template size as the output size when a template is provided
* Uses canvas width and height when no template is provided
* Supports pixel offsets from the center with `--offset-x` and `--offset-y`
* Supports relative product scaling with `--product-scale`
* Supports optional background removal with `--remove-bg`
* Supports background removal backend selection with `--bg-backend`
* Correctly pastes transparent RGBA images using an alpha mask
* Saves processed images to an output folder
* Creates the output folder automatically
* Shows friendly errors for missing input folders
* Shows friendly errors for empty input folders
* Skips broken images without stopping batch processing
* Prints processed and failed image counts
* Uses high-quality resize with LANCZOS
* Supports `--no-upscale` mode for keeping small images at their original size

## Supported file extensions

* `.jpg`
* `.jpeg`
* `.png`
* `.webp`

## Requirements

The project uses `rembg` with CPU support for background removal.

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to run

Basic usage:

```bash
python -m app.cli --input data/input --output data/output
```

Use a custom canvas size:

```bash
python -m app.cli --canvas-width 1200 --canvas-height 1600
```

Use relative product scaling:

```bash
python -m app.cli --product-scale 0.8
```

Use a custom template/background:

```bash
python -m app.cli --template data/template.png
```

Use a template with relative product scaling:

```bash
python -m app.cli --template data/template.png --product-scale 0.6
```

Remove product background before placing it on the template:

```bash
python -m app.cli --remove-bg --template data/template.png --product-scale 0.6
```

Remove product background with a selected backend:

```bash
python -m app.cli --remove-bg --bg-backend rembg --template data/template.png --product-scale 0.6
```

Disable upscaling for small images:

```bash
python -m app.cli --no-upscale
```

Move the product from the center using pixel offsets:

```bash
python -m app.cli --template data/template.png --offset-y -100
```

```bash
python -m app.cli --offset-x 50 --offset-y -120
```

Show all available CLI options:

```bash
python -m app.cli --help
```

## Example result

The tool can take a source product image, remove its background, resize it relative to a template, and place it on a marketplace-style product card.

Example command:

```bash
python -m app.cli --remove-bg --bg-backend rembg --template data/template.png --product-scale 0.6
```

## Planned features

* Reuse rembg sessions for faster batch processing
* Support multiple background removal models
* Compare background removal models by quality and speed
* Add alpha matting options for better edge quality
* Add mask diagnostics mode
* Processing report export
* Parallel image processing
* Docker support
* FastAPI backend
* Web interface

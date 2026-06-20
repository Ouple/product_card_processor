# Product Card Processor

A Python CLI tool for preparing product images for marketplace cards.

## Current version

v0.8 — template/background support

## Features

* Processes all supported images from an input folder
* Supports batch image processing
* Resizes each image to fit within configurable size limits
* Places each image on a configurable canvas
* Saves processed images to an output folder
* Creates the output folder automatically
* Shows friendly errors for missing input folders
* Shows friendly errors for empty input folders
* Skips broken images without stopping batch processing
* Prints processed and failed image counts
* Uses high-quality resize with LANCZOS
* Supports `--no-upscale` mode for keeping small images at their original size
- Supports custom template/background images
- When a template is provided, output size is based on the template size
- When no template is provided, canvas width and height are used
- Pixel offsets from center with --offset-x and --offset-y

## Supported file extensions

* `.jpg`
* `.jpeg`
* `.png`
* `.webp`

## How to run

Basic usage:

```bash
python -m app.cli --input data/input --output data/output
```

Custom canvas and product size:

```bash
python -m app.cli --canvas-width 1200 --canvas-height 1600 --max-image-width 1000 --max-image-height 1300
```
User Template

```bash
python -m app.cli --template data/template.png
```

Disable upscaling for small images:

```bash
python -m app.cli --no-upscale
```

Show all available CLI options:

```bash
python -m app.cli --help
```
Pixel offsets from center with --offset-x and --offset-y

```bash
python -m app.cli --template data/template.png --offset-y -100
python -m app.cli --offset-x 50 --offset-y -120
```
## Planned features

* Optional background removal
* Processing report export
* Parallel image processing
* Docker support
* Web interface

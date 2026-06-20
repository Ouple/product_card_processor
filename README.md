# Product Card Processor

A Python CLI tool for preparing product images for marketplace cards.

## Current version

v0.7 — improved resize behavior

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

Disable upscaling for small images:

```bash
python -m app.cli --no-upscale
```

Show all available CLI options:

```bash
python -m app.cli --help
```

## Planned features

* Frame/template support
* Product positioning settings
* Optional background removal
* Processing report export
* Parallel image processing
* Docker support
* Web interface

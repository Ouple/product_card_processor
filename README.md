# Product Card Processor

A Python CLI tool for preparing product images for marketplace cards.

- processes all images from data/input
- resizes each image to fit within 900x1200
- places it on a 1080x1440 white canvas
- saves results to data/output

- creates output folder automatically
- shows friendly errors for missing input folder
- shows friendly errors for empty input folder
- skips broken images without stopping batch processing
- prints processed and failed counts

## Current version

v0.6 — friendly error handling

## Planned features

- Batch image processing
- Product image resizing
- Canvas generation
- Frame/template support
- Optional background removal
- Docker support

## How to run

python -m app.cli --input data/input --output data/output

python -m app.cli --canvas-width 1200 --canvas-height 1600 --max-image-width 1000 --max-image-height 1300

supported file extensions:
.jpg, .jpeg, .png, .webp
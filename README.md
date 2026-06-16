# Product Card Processor

A Python CLI tool for preparing product images for marketplace cards.

- processes all images from data/input
- resizes each image to fit within 900x1200
- places it on a 1080x1440 white canvas
- saves results to data/output

## Current version

v0.4 — centered product card generation

## Planned features

- Batch image processing
- Product image resizing
- Canvas generation
- Frame/template support
- Optional background removal
- Docker support

## How to run

Place images into:
data/input

Run:
python -m app.cli

Processed images will be saved to:
data/output

supported file extensions:
.jpg, .jpeg, .png, .webp
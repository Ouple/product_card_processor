# Product Card Processor

A Python CLI tool for preparing product images for marketplace cards.

The tool can batch-process product images, resize them relative to a canvas or template, optionally remove the background with neural network models, and place the product image onto a marketplace-style card.

## Current version

v0.13 — background removal model selection

## Features

* Processes all supported images from an input folder
* Supports batch image processing
* Resizes product images relative to the canvas or template size
* Places product images on a configurable canvas or custom template
* Supports custom template/background images
* Uses the template size as the output size when a template is provided
* Uses canvas width and height when no template is provided
* Supports relative product scaling with `--product-scale`
* Supports pixel offsets from the center with `--offset-x` and `--offset-y`
* Supports optional background removal with `--remove-bg`
* Supports background removal backend selection with `--bg-backend`
* Supports background removal model selection with `--bg-model`
* Reuses rembg sessions for faster batch processing
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

Background removal models are downloaded automatically on first use. Large models may require additional disk space and may take longer to download.

## Basic usage

Process images from the default input folder and save results to the default output folder:

```bash
python -m app.cli --input data/input --output data/output
```

Show all available CLI options:

```bash
python -m app.cli --help
```

## Canvas and template options

Use a custom canvas size:

```bash
python -m app.cli --canvas-width 1200 --canvas-height 1600
```

Use a custom template/background:

```bash
python -m app.cli --template data/template.png
```

When a template is provided, the output image size is based on the template size.

## Product scaling and positioning

Resize the product relative to the canvas or template size:

```bash
python -m app.cli --product-scale 0.8
```

Use a template with relative product scaling:

```bash
python -m app.cli --template data/template.png --product-scale 0.6
```

Move the product from the center using pixel offsets:

```bash
python -m app.cli --template data/template.png --offset-y -100
```

```bash
python -m app.cli --template data/template.png --offset-x 50 --offset-y -120
```

Disable upscaling for small images:

```bash
python -m app.cli --no-upscale
```

## Background removal

Remove product background before placing it on the canvas or template:

```bash
python -m app.cli --remove-bg --template data/template.png --product-scale 0.6
```

Remove product background with the selected backend:

```bash
python -m app.cli --remove-bg --bg-backend rembg --template data/template.png --product-scale 0.6
```

Select a background removal model:

```bash
python -m app.cli --remove-bg --bg-model u2net --template data/template.png --product-scale 0.6
```

```bash
python -m app.cli --remove-bg --bg-model isnet-general-use --template data/template.png --product-scale 0.6
```

```bash
python -m app.cli --remove-bg --bg-model birefnet-general --template data/template.png --product-scale 0.6
```

## Supported background removal models

| Model               | Description                                      | Notes                                                                                      |
| ------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `u2net`             | Default general-purpose background removal model | Good baseline model                                                                        |
| `isnet-general-use` | General-purpose object segmentation model        | Useful alternative to `u2net`                                                              |
| `birefnet-general`  | Larger general-purpose segmentation model        | May provide better quality, but requires significantly more disk space and processing time |

## Model comparison workflow

To compare background removal models, process the same input folder with different models and save the results into separate output folders.

### U2Net

```bash
python -m app.cli --remove-bg --bg-model u2net --template data/template.png --product-scale 0.6 --output data/output/u2net
```

### IS-Net general use

```bash
python -m app.cli --remove-bg --bg-model isnet-general-use --template data/template.png --product-scale 0.6 --output data/output/isnet-general-use
```

### BiRefNet general

```bash
python -m app.cli --remove-bg --bg-model birefnet-general --template data/template.png --product-scale 0.6 --output data/output/birefnet-general
```

## Model comparison criteria

The models can be compared by:

* object edge quality
* preservation of small details
* handling of holes and inner cutouts
* shadow and reflection removal
* processing speed
* model size and disk space usage
* stability on different product types

## Current observations

`u2net` is a good default baseline model.

`isnet-general-use` can produce different masks and should be tested on real product images before choosing a default.

`birefnet-general` may provide higher-quality segmentation on difficult images, but it is much heavier than the other options and may be slower to download and run.

For production usage, model choice should depend on the trade-off between quality, speed, and disk space.

## Example result

The tool can take a source product image, remove its background, resize it relative to a template, and place it on a marketplace-style product card.

Example command:

```bash
python -m app.cli --remove-bg --bg-backend rembg --bg-model u2net --template data/template.png --product-scale 0.6
```

## Planned features

* Add alpha matting options for better edge quality
* Add mask diagnostics mode
* Add processing report export
* Add parallel image processing
* Add Docker support
* Add FastAPI backend
* Add web interface

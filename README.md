# Product Card Processor

A Python CLI tool for preparing product images for marketplace cards.

The tool can batch-process product images, resize them relative to a canvas or template, optionally remove the background with neural network models, and place the product image onto a marketplace-style card.

## Current version

v0.14 — background removal model comparison

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

Background removal models are downloaded automatically on first use.

Large models may require additional disk space and may take longer to download. For example, `birefnet-general` is significantly heavier than the default model.

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

| Model               | Description                                      | Notes                                                          |
| ------------------- | ------------------------------------------------ | -------------------------------------------------------------- |
| `u2net`             | Default general-purpose background removal model | Good lightweight baseline                                      |
| `isnet-general-use` | General-purpose object segmentation model        | Best balance in the current tests                              |
| `birefnet-general`  | Larger general-purpose segmentation model        | Best quality in the current tests, but much heavier and slower |

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

## Performance measurement

Processing time was measured locally with PowerShell `Measure-Command`.

Example:

```powershell
Measure-Command { python -m app.cli --remove-bg --bg-model u2net --template data/template.png --product-scale 0.6 --output data/output/u2net }
```

The measurements below are based on the current local test set and environment. Actual results may vary depending on hardware, image resolution, number of files, and whether the model has already been downloaded.

| Model               | Total time, seconds |            Relative speed | Notes                                 |
| ------------------- | ------------------: | ------------------------: | ------------------------------------- |
| `u2net`             |                6.85 |                      1.0x | Fastest tested model                  |
| `isnet-general-use` |               12.89 |  1.9x slower than `u2net` | Slower, but better quality            |
| `birefnet-general`  |              185.24 | 27.0x slower than `u2net` | Best quality, but very slow and heavy |

## Model comparison criteria

The models were compared manually using real automotive product images.

The main criteria were:

* object edge quality
* preservation of small details
* handling of holes and inner cutouts
* shadow and reflection removal
* processing speed
* model size and disk space usage
* stability on different product types

## Current observations

The following models were tested:

* `u2net`
* `isnet-general-use`
* `birefnet-general`

### U2Net

`u2net` works as a solid baseline model.

It handles simple product shapes reasonably well, but it shows weaker results on more difficult geometry, especially inner cutouts, holes, and complex object boundaries.

It was the fastest model in the current test run.

Recommended role:

* lightweight baseline
* fastest tested option
* useful when speed and model size matter more than maximum quality

### IS-Net general use

`isnet-general-use` produced cleaner masks than `u2net` in the tested examples.

It handled several product images more accurately and provided a better balance between quality and practical usability.

It was slower than `u2net`, but still much faster than `birefnet-general`.

Recommended role:

* best balanced option
* good candidate for the default model
* suitable for regular batch processing

### BiRefNet general

`birefnet-general` produced the best masks in the tested examples.

It handled complex product geometry and inner cutouts better than the other tested models. However, it is significantly heavier and much slower.

In the current test run, it was about 27 times slower than `u2net`.

Recommended role:

* best quality option
* useful for difficult product images
* suitable when quality is more important than speed and model size

## Model comparison summary

| Model               | Quality   | Speed     | Practicality | Notes                                                 |
| ------------------- | --------- | --------- | ------------ | ----------------------------------------------------- |
| `u2net`             | Medium    | Fast      | High         | Good lightweight baseline, weaker on difficult shapes |
| `isnet-general-use` | High      | Medium    | High         | Best balance between quality and usability            |
| `birefnet-general`  | Very high | Very slow | Medium       | Best quality, but heavy and much slower               |

## Recommended usage

For most regular product images:

```bash
python -m app.cli --remove-bg --bg-model isnet-general-use --template data/template.png --product-scale 0.6
```

For faster lightweight processing:

```bash
python -m app.cli --remove-bg --bg-model u2net --template data/template.png --product-scale 0.6
```

For best quality on difficult product images:

```bash
python -m app.cli --remove-bg --bg-model birefnet-general --template data/template.png --product-scale 0.6
```

## Example result

The tool can take a source product image, remove its background, resize it relative to a template, and place it on a marketplace-style product card.

Example command:

```bash
python -m app.cli --remove-bg --bg-backend rembg --bg-model isnet-general-use --template data/template.png --product-scale 0.6
```

## Project roadmap

### Completed

* `v0.1` — project structure
* `v0.2` — single image processing
* `v0.3` — batch image processing
* `v0.4` — centered product card generation
* `v0.5` — configurable CLI arguments
* `v0.6` — friendly error handling
* `v0.7` — improved resize behavior and `--no-upscale`
* `v0.8` — template/background support
* `v0.9` — pixel offsets from center
* `v0.10` — relative product scaling
* `v0.11` — background removal with rembg backend
* `v0.12` — rembg session reuse for faster batch processing
* `v0.13` — background removal model selection
* `v0.14` — background removal model comparison

### Planned features

* Add alpha matting options for better edge quality
* Add post-processing options for masks
* Add mask diagnostics mode
* Add processing report export
* Add parallel image processing
* Add Docker support
* Add FastAPI backend
* Add web interface

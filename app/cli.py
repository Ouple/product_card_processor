import argparse
from pathlib import Path

from app.processor import ImageProcessor

from app.config import INPUT_FOLDER, OUTPUT_FOLDER, CANVAS_WIDTH, CANVAS_HEIGHT

def parse_args():
    parser = argparse.ArgumentParser(
        description='Product card image processor'
    )
    parser.add_argument("--input",
                        type=Path,
                        default=INPUT_FOLDER,
                        help='Input folder with source images'
                        )

    parser.add_argument("--output",
                        type=Path,
                        default=OUTPUT_FOLDER,
                        help='Output folder for processed images'
                        )

    parser.add_argument("--canvas-width",
                        type=int,
                        default=CANVAS_WIDTH,
                        help='Canvas width in pixels'
                        )

    parser.add_argument("--canvas-height",
                        type=int,
                        default=CANVAS_HEIGHT,
                        help='Canvas height in pixels'
                        )
    parser.add_argument("--no-upscale",
                        action="store_true",
                        help='no upscale mode, do not enlarge images smaller than the target size'
                        )
    parser.add_argument("--template",
                        type=Path,
                        default=None,
                        help="Template/background image path"
                        )
    parser.add_argument("--offset-x",
                        type=int,
                        default=0,
                        help="Horizontal offset from center in pixels"
                        )
    parser.add_argument("--offset-y",
                        type=int,
                        default=0,
                        help="Vertical offset from center in pixels")
    parser.add_argument("--product-scale",
                        type=float,
                        default=0.8,
                        help="Product size scale factor, product size relative to background size, from 0 to 1")

    return parser.parse_args()

args = parse_args()

processor = ImageProcessor(
    input_folder=args.input,
    output_folder=args.output,
    canvas_width=args.canvas_width,
    canvas_height=args.canvas_height,
    allow_upscale=not args.no_upscale,
    template_path = args.template,
    offset_x=args.offset_x,
    offset_y=args.offset_y,
    product_scale=args.product_scale
    )

try:
    processed_count = processor.process_all_images()
    print(f"Processed images {processed_count}")
    print(f"Failed images {processor.failed_count}")

except FileNotFoundError as error:
    print(error)
except NotADirectoryError as error:
    print(error)
except ValueError as error:
    print(error)





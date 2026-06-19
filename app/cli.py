import argparse
from pathlib import Path

from app.processor import ImageProcessor

from app.config import INPUT_FOLDER, OUTPUT_FOLDER, CANVAS_WIDTH, CANVAS_HEIGHT, MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT

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

    parser.add_argument("--max-image-width",
                        type=int,
                        default=MAX_IMAGE_WIDTH,
                        help='Max image width in pixels'
                        )

    parser.add_argument("--max-image-height",
                        type=int,
                        default=MAX_IMAGE_HEIGHT,
                        help='Max image height in pixels'
                        )

    return parser.parse_args()

args = parse_args()

processor = ImageProcessor(args.input,
                           args.output,
                           args.canvas_width,
                           args.canvas_height,
                           args.max_image_width,
                           args.max_image_height)

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





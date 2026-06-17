from app.processor import ImageProcessor

from app.config import INPUT_FOLDER, OUTPUT_FOLDER, CANVAS_WIDTH, CANVAS_HEIGHT, MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT

processor = ImageProcessor(INPUT_FOLDER,
                           OUTPUT_FOLDER,
                           CANVAS_WIDTH,
                           CANVAS_HEIGHT,
                           MAX_IMAGE_WIDTH,
                           MAX_IMAGE_HEIGHT)

processed_count = processor.process_all_images()
print(f"Processed images {processed_count}")





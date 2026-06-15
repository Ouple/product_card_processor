from app.image_io import load_image, save_image

input_path = "data/input/test.jpg"
output_path = "data/output/result.jpg"

image = load_image(input_path)

print("Product card processor started")
print(f"image size: {image.size}")

save_image(image, output_path)

print(f"Image saved to: {output_path}")
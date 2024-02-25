from PIL import Image, ImageFilter

# Open an image file
image = Image.open("input_image.jpg")

# Resize the image
resized_image = image.resize((300, 200))

# Crop a region from the image
cropped_image = image.crop((100, 100, 400, 300))

# Rotate the image by 90 degrees
rotated_image = image.rotate(90)

# Apply a Gaussian blur filter
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5))

# Save manipulated images
resized_image.save("resized_image.jpg")
cropped_image.save("cropped_image.jpg")
rotated_image.save("rotated_image.jpg")
blurred_image.save("blurred_image.jpg")

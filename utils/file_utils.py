from django.core.exceptions import ValidationError
from drf_orm.settings import FILE_UPLOAD_MAX_MEMORY_SIZE
from rest_framework import serializers
from PIL import Image
from io import BytesIO
import os


def validate_image_extension(image):
    allowed_extensions = ['jpeg', 'jpg', 'png', 'gif']
    extension = image.name.split('.')[-1].lower()

    if extension not in allowed_extensions:
        raise ValidationError(
            "Invalid image format. Please upload a valid image file (JPG, JPEG, PNG, GIF)."
        )


# Calculate the maximum file size in bytes
# 2.5 MB (2.5 * 1024 * 1024 bytes)
def max_file_size_validator(value):
    max_size_byte = FILE_UPLOAD_MAX_MEMORY_SIZE
    max_size_mb = max_size_byte / (1024**2)

    print('max_size_mb:', value.size / (1024**2))

    if value.size > max_size_byte:
        raise ValidationError(f'File size cannot exceed {max_size_mb} MB.')


def custom_cover_image_filename(instance, filename):
    # Modify the file name as needed
    book_id = instance.id  # Assuming your Book model has an 'id' field
    if book_id is None:
        # If the book is new and doesn't have an ID yet, use a temporary identifier
        book_id = "new_book"
    ext = filename.split('.')[-1]  # Get the file extension
    new_filename = f'book_{book_id}_cover.{ext}'  # Customize the new file name
    return os.path.join('book_covers/', new_filename)


def compress_image(self, image):
    try:
        # Open the image using Pillow
        img = Image.open(image)

        # Perform image compression or other processing here
        # Example: Resizing the image to a specific size
        img.thumbnail((400, 400))

        # Save the processed image to a BytesIO buffer
        output = BytesIO()
        img.save(output, format='JPEG', quality=75)

        # Rewind the buffer to the beginning
        output.seek(0)

        # Return the processed image
        return output
    except Exception as e:
        # Handle any exceptions that may occur during image processing
        raise serializers.ValidationError("Error processing the image.")

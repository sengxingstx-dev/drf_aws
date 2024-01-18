from django.db.models.signals import pre_save, pre_delete, post_save
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from .models import Book
from rest_framework import serializers
from django.core.files import File


# pre_save: before saving or before updating
@receiver(pre_save, sender=Book)
def delete_cover_image_on_update(sender, instance, **kwargs):
    # Check if the instance is being updated
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.cover_image:
                # Delete the old cover image when a book is updated
                old_instance.cover_image.delete(save=False)
        except sender.DoesNotExist:
            pass


@receiver(pre_delete, sender=Book)
def delete_cover_image_on_delete(sender, instance, **kwargs):
    # Delete the cover image when a book is deleted
    if instance.cover_image:
        instance.cover_image.delete(save=False)


@receiver(pre_save, sender=Book)
def compress_image(sender, instance, **kwargs):
    try:
        # Open image and determine format
        with Image.open(instance.cover_image) as im:
            img_format = im.format

            # If image is JPEG, compress using JPEG format
            if img_format == 'JPEG':
                # Save the compressed image to BytesIO object
                im.thumbnail((400, 400))
                im_io = BytesIO()
                im.save(im_io, 'JPEG', quality=70)
                # Create a django-friendly Files object
                new_image = File(im_io, name=instance.cover_image.name)

            # If image is PNG, compress using PNG format
            elif img_format == 'PNG':
                # Save the compressed image to BytesIO object
                im.thumbnail((400, 400))
                im_io = BytesIO()
                im.save(im_io, 'PNG', optimize=True)
                # Create a django-friendly Files object
                new_image = File(im_io, name=instance.cover_image.name)

            # If image is neither JPEG nor PNG, raise an exception
            else:
                raise Exception(f'Unsupported image format: {img_format}')

            # Assign the compressed image back to the instance's cover_image attribute
            instance.cover_image = new_image
    except Exception as e:
        # Handle any exceptions that may occur during image processing
        raise serializers.ValidationError(f'Error processing the image. {str(e)}')

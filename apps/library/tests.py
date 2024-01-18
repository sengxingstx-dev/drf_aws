from django.test import TestCase
from apps.library.serializers import BookSerializer
from drf_orm.settings import FILE_UPLOAD_MAX_MEMORY_SIZE


class BookSerializerTest(TestCase):
    def test_validate_image_file(self):
        serializer = BookSerializer(data={'title': 'My Book', 'cover_image': 'my_image.png'})
        serializer.is_valid()
        self.assertEqual(serializer.validated_data['cover_image'].name, 'my_image.png')

    def test_max_file_size_validator(self):
        serializer = BookSerializer(data={'title': 'My Book', 'cover_image': 'my_image.png'})
        serializer.is_valid()
        self.assertEqual(serializer.validated_data['cover_image'].size, 1024**2)

    def test_invalid_image_file(self):
        serializer = BookSerializer(data={'title': 'My Book', 'cover_image': 'my_image.txt'})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors['cover_image'][0], 'Please upload a valid image file (JPG, PNG, GIF).'
        )

    def test_file_too_large(self):
        serializer = BookSerializer(data={'title': 'My Book', 'cover_image': 'my_image.png'})
        serializer.validated_data['cover_image'].size = FILE_UPLOAD_MAX_MEMORY_SIZE + 1
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors['cover_image'][0], 'File size cannot exceed 2.5 MB.')

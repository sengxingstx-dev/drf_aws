from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .models import Author, Publisher, Genre, Book
from .serializers import AuthorSerializer, PublisherSerializer, GenreSerializer, BookSerializer


# Create your views here.
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherListCreateView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


from rest_framework.parsers import MultiPartParser, FormParser


# Using ViewSets
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # parser_classes = (MultiPartParser, FormParser)

    # def perform_create(self, serializer):
    #     cover_image = self.request.data.get('cover_image')
    #     if cover_image:
    #         serializer.save(cover_image=cover_image)
    #     else:
    #         serializer.save()

    # def perform_update(self, serializer):
    #     cover_image = self.request.data.get('cover_image')
    #     if cover_image:
    #         serializer.save(cover_image=cover_image)
    #     else:
    #         serializer.save()

    # def perform_destroy(self, instance):
    #     if instance.cover_image:
    #         instance.cover_image.delete()
    #     instance.delete()

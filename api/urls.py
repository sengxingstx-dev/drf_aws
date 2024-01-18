from django.urls import path
from rest_framework import routers
from .views import APIRootView
from apps.library.views import (
    AuthorListCreateView,
    AuthorDetailView,
    PublisherListCreateView,
    PublisherDetailView,
    GenreListCreateView,
    GenreDetailView,
    BookViewSet,
)

router = routers.DefaultRouter()

router.register('books', BookViewSet)

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('publishers/', PublisherListCreateView.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher-detail'),
    path('genres/', GenreListCreateView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
    # path('books/', include(router.urls)),
]

urlpatterns += router.urls

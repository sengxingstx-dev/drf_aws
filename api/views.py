from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.reverse import reverse


# Create your views here.
class APIRootView(APIView):
    queryset = None

    def get(self, request, format=None):
        return Response(
            {
                'authors': reverse('author-list', request=request, format=format),
                'publishers': reverse('publisher-list', request=request, format=format),
                'genres': reverse('genre-list', request=request, format=format),
                'books': reverse('book-list', request=request, format=format),
            }
        )

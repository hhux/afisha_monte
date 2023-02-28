from django.http import HttpResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import FacebookPost
from .serializers import FacebookPostSerializer, FacebookCreatePostSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class FacebookPostsRetrieveView(generics.RetrieveAPIView):
    """"
    Дженерик получения всех постов FacebookPost
    """
    queryset = FacebookPost.objects.all()
    serializer_class = FacebookPostSerializer


class FacebookPostRetrieveView(generics.RetrieveAPIView):
    """
    Дженерик получения одного поста FacebookPost по айди
    """
    queryset = FacebookPost.objects.all()
    serializer_class = FacebookPostSerializer


class FacebookCreatePostView(generics.CreateAPIView):
    """"
    Дженерик создания объекта Post
    """
    queryset = FacebookPost.objects.all()
    serializer_class = FacebookCreatePostSerializer
    # уточним по поводу функционала на разных пользаках системы
    # permission_classes = (permissions.IsAuthenticated,)


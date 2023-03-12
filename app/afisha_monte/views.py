from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .fb_module import get_last_fb_post
from .models import FacebookPost, FacebookUrl
from .serializers import FacebookPostSerializer, FacebookCreatePostSerializer, FacebookUrlSerializer
from .utils import generate_id


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class FacebookPostsRetrieveView(generics.ListAPIView):
    """"
    Дженерик получения всех постов FacebookPost
    """
    queryset = FacebookPost.objects.all()
    serializer_class = FacebookPostSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    filterset_fields = ['is_active', 'is_approved']


class FacebookPostRetrieveView(generics.RetrieveAPIView):
    """
    Дженерик получения одного поста FacebookPost по айди
    """
    queryset = FacebookPost.objects.all()
    serializer_class = FacebookPostSerializer
    permission_classes = [IsAuthenticated]


class FacebookCreatePostView(generics.CreateAPIView):
    """"
    Дженерик создания объекта Post
    """
    queryset = FacebookPost.objects.all()
    serializer_class = FacebookCreatePostSerializer
    permission_classes = [IsAuthenticated]
    # уточним по поводу функционала на разных пользаках системы
    # permission_classes = (permissions.IsAuthenticated,)


class FacebookUrlRetrieveView(generics.RetrieveAPIView):
    """"
    Дженерик чтения объекта Url по айди
    """
    queryset = FacebookUrl.objects.all()
    serializer_class = FacebookUrlSerializer
    permission_classes = [IsAuthenticated]


class FacebookUrlsRetrieveView(generics.ListAPIView):
    """"
    Дженерик чтения всех объектов Url
    """
    queryset = FacebookUrl.objects.all()
    serializer_class = FacebookUrlSerializer
    permission_classes = [IsAuthenticated]


class FacebookCreateUrlView(generics.CreateAPIView):
    """"
    Дженерик создания объекта Url
    """
    queryset = FacebookPost.objects.all()
    serializer_class = FacebookUrlSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs) -> Response:
        """
        Функция создания поста по урлу
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            facebook_url = serializer.save()
            fb_post = get_last_fb_post(serializer.data['url'])
            fb_post = {k: v for k, v in fb_post.items() if k in FacebookPost.get_model_fields()}
            fb_post.update({'facebook_url_id': facebook_url})
            fb_post.update({'post_id': generate_id((fb_post['text'], fb_post['time'], fb_post['timestamp']))})
            post = FacebookPost(**fb_post)
            post.save()
        return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def check_posts(request):
    updated_posts = []

    all_facebook_urls = FacebookUrl.objects.all()

    if not all_facebook_urls:
        return

    for facebook_url in all_facebook_urls:
        fb_post = get_last_fb_post(facebook_url.url)
        fb_post_id = generate_id((fb_post['text'], fb_post['time'], fb_post['timestamp']))
        last_post = FacebookPost.objects.filter(post_id=fb_post_id)
        if not last_post:
            all_facebook_posts = FacebookPost.objects.filter(post_url=facebook_url)
            for post in all_facebook_posts:
                post.is_active = False
                post.save()
            fb_post = {k: v for k, v in fb_post.items() if k in FacebookPost.get_model_fields()}
            fb_post.update({'post_id': generate_id((fb_post['text'], fb_post['time'], fb_post['timestamp']))})
            fb_post.update({'facebook_url_id': facebook_url})
            new_post = FacebookPost(**fb_post)
            new_post.is_active = True
            new_post.save()
            updated_posts.append(new_post)

    return Response(status=status.HTTP_200_OK)

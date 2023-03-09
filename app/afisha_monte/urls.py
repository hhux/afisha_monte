from django.contrib import admin
from django.urls import path, include

from .views import FacebookPostRetrieveView, FacebookPostsRetrieveView, FacebookCreatePostView, FacebookCreateUrlView, \
    FacebookUrlsRetrieveView, FacebookUrlRetrieveView, test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('facebook_post/<uuid:pk>/', FacebookPostRetrieveView.as_view()),
    path('facebook_posts/', FacebookPostsRetrieveView.as_view()),
    path('facebook_post/new', FacebookCreatePostView.as_view()),
    path('facebook_url/<uuid:pk>/', FacebookUrlRetrieveView.as_view()),
    path('facebook_urls/', FacebookUrlsRetrieveView.as_view()),
    path('facebook_url/new', FacebookCreateUrlView.as_view()),
    path('test/', test, name="test")
]

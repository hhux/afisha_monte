from django.contrib import admin
from django.urls import path

from .views import FacebookPostRetrieveView, FacebookPostsRetrieveView, FacebookCreatePostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('facebook_post/<uuid:pk>/', FacebookPostRetrieveView.as_view()),
    path('facebook_posts/', FacebookPostsRetrieveView.as_view()),
    path('facebook_post/new', FacebookCreatePostView.as_view()),

]

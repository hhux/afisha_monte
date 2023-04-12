from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import FacebookPostRetrieveView, FacebookPostsRetrieveView, FacebookCreatePostView, FacebookCreateUrlView, \
    FacebookUrlsRetrieveView, FacebookUrlRetrieveView, check_posts, FacebookPostUpdateView, FacebookPostDeleteView, \
    FacebookUrlDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    # ------- posts ---------
    path('facebook_post/<uuid:pk>/', FacebookPostRetrieveView.as_view()),
    path('facebook_posts/', FacebookPostsRetrieveView.as_view()),
    path('facebook_post/new', FacebookCreatePostView.as_view()),
    path('facebook_post/<uuid:pk>/update', FacebookPostUpdateView.as_view()),
    path('facebook_post/<uuid:pk>/delete', FacebookPostDeleteView.as_view()),

    # ------- urls ---------
    path('facebook_url/<uuid:pk>/', FacebookUrlRetrieveView.as_view()),
    path('facebook_urls/', FacebookUrlsRetrieveView.as_view()),
    path('facebook_url/new', FacebookCreateUrlView.as_view()),
    path('facebook_url/<uuid:pk>/delete', FacebookUrlDeleteView.as_view()),

    # ------- auth ---------
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('check_posts/', check_posts, name="check_posts")
]

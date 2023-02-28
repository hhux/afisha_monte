from django.contrib import admin

from .models import FacebookPost, FacebookUrl

# регистрируем модели
admin.site.register(FacebookPost)
admin.site.register(FacebookUrl)

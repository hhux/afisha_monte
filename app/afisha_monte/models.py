import uuid

from django.db import models


class FacebookPost(models.Model):
    """
    Модель Post - пост с фейсбука

    fields:
    original_request_url: str
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    original_request_url = models.CharField(max_length=512)
    post_url = models.CharField(max_length=512)
    post_id = models.CharField(max_length=512)
    text = models.CharField(max_length=512)
    post_text = models.CharField(max_length=512)
    shared_text = models.CharField(max_length=512)
    original_text = models.BooleanField()
    time = models.DateTimeField()
    timestamp = models.IntegerField()
    image = models.BooleanField()
    image_lowquality = models.CharField(max_length=512)
    images = models.CharField(max_length=512)
    images_description = models.CharField(max_length=512)
    images_lowquality = models.CharField(max_length=512)

    video = models.CharField(max_length=512)
    video_id = models.CharField(max_length=512)
    video_watches = models.BooleanField()
    likes = models.IntegerField()
    comments = models.IntegerField()
    shares = models.IntegerField()


class FacebookUrl(models.Model):
    """
    Модель Urls. Содержит урл по которому скрипт будет парсить посты
    """
    url = models.CharField(max_length=512)

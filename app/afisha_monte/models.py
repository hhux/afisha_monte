import uuid

from django.db import models


class FacebookUrl(models.Model):
    """
    Модель Urls. Содержит урл по которому скрипт будет парсить посты
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=2048, unique=True)
    created = models.DateTimeField(auto_now=True)


class FacebookPost(models.Model):
    """
    Модель Post - пост с фейсбука
    """
    # эти поля будут заполняться администратором системы
    city = models.CharField(max_length=2048, null=True, required=False)
    place = models.CharField(max_length=2048, null=True, required=False)
    address = models.CharField(max_length=2048, null=True, required=False)
    phone = models.CharField(max_length=2048, null=True, required=False)
    date = models.DateTimeField(null=True, required=False)
    time = models.CharField(max_length=2048, null=True, required=False)
    event_type = models.CharField(max_length=2048, null=True, required=False)
    artist = models.CharField(max_length=2048, null=True, required=False)
    event_description = models.CharField(max_length=2048, null=True, required=False)
    picture = models.ImageField(null=True, required=False)
    reserved_field = models.CharField(max_length=2048, null=True, required=False)
    reserved_field_2 = models.CharField(max_length=2048, null=True, required=False)

    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    # поля приходящие с фейсбука
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    facebook_url_id = models.ForeignKey(FacebookUrl, on_delete=models.CASCADE, related_name='facebook_url_id', null=True)

    created = models.DateTimeField(auto_now=True)
    original_request_url = models.CharField(max_length=2048, null=True, required=False)
    post_url = models.CharField(max_length=2048, null=True, required=False)
    post_id = models.UUIDField(null=True, required=False)
    text = models.CharField(max_length=2048, null=True, required=False)
    post_text = models.CharField(max_length=2048, null=True, required=False)
    shared_text = models.CharField(max_length=2048, null=True, required=False)
    original_text = models.CharField(max_length=2048, null=True, required=False)
    time = models.DateTimeField(null=True, required=False)
    timestamp = models.IntegerField(null=True)
    image = models.CharField(max_length=2048, null=True, required=False)
    image_lowquality = models.CharField(max_length=2048, null=True, required=False)
    images = models.CharField(max_length=2048, null=True, required=False)
    images_description = models.CharField(max_length=2048, null=True, required=False)
    images_lowquality = models.CharField(max_length=2048, null=True, required=False)
    images_lowquality_description = models.CharField(max_length=2048, null=True, required=False)

    video = models.CharField(max_length=2048, null=True, required=False)
    video_id = models.CharField(max_length=2048, null=True, required=False)
    video_watches = models.BooleanField(null=True)
    likes = models.IntegerField(null=True)
    comments = models.IntegerField(null=True)
    shares = models.IntegerField(null=True)

    @classmethod
    def get_model_fields(cls):
        return [field.name for field in cls._meta.fields]

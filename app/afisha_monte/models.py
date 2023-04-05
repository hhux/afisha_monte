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

    fields:
    original_request_url: str
    #TODO уточнить у заказчика какие поля будем сохранять + дописать аннотацию типов
    """
    # эти поля будут заполняться администратором системы
    city = models.CharField(max_length=2048, null=True)
    place = models.CharField(max_length=2048, null=True)
    address = models.CharField(max_length=2048, null=True)
    phone = models.CharField(max_length=2048, null=True)
    date = models.DateTimeField(null=True)
    time = models.CharField(max_length=2048, null=True)
    event_type = models.CharField(max_length=2048, null=True)
    artist = models.CharField(max_length=2048, null=True)
    event_description = models.CharField(max_length=2048, null=True)
    picture = models.ImageField(null=True)
    reserved_field = models.CharField(max_length=2048, null=True)
    reserved_field_2 = models.CharField(max_length=2048, null=True)

    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    # поля приходящие с фейсбука
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    facebook_url_id = models.ForeignKey(FacebookUrl, on_delete=models.CASCADE, related_name='facebook_url_id', null=True)

    created = models.DateTimeField(auto_now=True)
    original_request_url = models.CharField(max_length=2048, null=True)
    post_url = models.CharField(max_length=2048, null=True)
    post_id = models.UUIDField(null=True)
    text = models.CharField(max_length=2048, null=True)
    post_text = models.CharField(max_length=2048, null=True)
    shared_text = models.CharField(max_length=2048, null=True)
    original_text = models.CharField(max_length=2048, null=True)
    time = models.DateTimeField(null=True)
    timestamp = models.IntegerField(null=True)
    image = models.CharField(max_length=2048, null=True)
    image_lowquality = models.CharField(max_length=2048, null=True)
    images = models.CharField(max_length=2048, null=True)
    images_description = models.CharField(max_length=2048, null=True)
    images_lowquality = models.CharField(max_length=2048, null=True)
    images_lowquality_description = models.CharField(max_length=2048, null=True)

    video = models.CharField(max_length=2048, null=True)
    video_id = models.CharField(max_length=2048, null=True)
    video_watches = models.BooleanField(null=True)
    likes = models.IntegerField(null=True)
    comments = models.IntegerField(null=True)
    shares = models.IntegerField(null=True)

    @classmethod
    def get_model_fields(cls):
        return [field.name for field in cls._meta.fields]

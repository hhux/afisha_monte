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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    facebook_url_id = models.ForeignKey(FacebookUrl, on_delete=models.CASCADE, related_name='facebook_url_id')

    created = models.DateTimeField(auto_now=True)
    original_request_url = models.CharField(max_length=2048)
    post_url = models.CharField(max_length=2048, null=True)
    post_id = models.UUIDField(null=True)
    text = models.CharField(max_length=2048, null=True)
    post_text = models.CharField(max_length=2048, null=True)
    shared_text = models.CharField(max_length=2048, null=True)
    original_text = models.CharField(max_length=2048, null=True)
    time = models.DateTimeField()
    timestamp = models.IntegerField()  # TODO проверить тип данных
    image = models.CharField(max_length=2048, null=True)
    image_lowquality = models.CharField(max_length=2048, null=True)
    images = models.CharField(max_length=2048, null=True)
    images_description = models.CharField(max_length=2048, null=True)
    images_lowquality = models.CharField(max_length=2048, null=True)
    images_lowquality_description = models.CharField(max_length=2048, null=True)

    video = models.CharField(max_length=2048, null=True)  # TODO !
    video_id = models.CharField(max_length=2048, null=True)
    video_watches = models.BooleanField(null=True)
    likes = models.IntegerField(null=True)
    comments = models.IntegerField(null=True)
    shares = models.IntegerField(null=True)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    @classmethod
    def get_model_fields(cls):
        return [field.name for field in cls._meta.fields]

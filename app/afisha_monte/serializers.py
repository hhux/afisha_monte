from rest_framework import serializers

from .models import FacebookPost, FacebookUrl


class FacebookPostSerializer(serializers.ModelSerializer):
    """"
    FacebookPost Сериализатор
    """

    class Meta:
        model = FacebookPost
        fields = '__all__'


class FacebookCreatePostSerializer(serializers.ModelSerializer):
    """
    Facebook Create Post Сериализатор
    """

    class Meta:
        model = FacebookPost
        fields = '__all__'


class FacebookUrlSerializer(serializers.ModelSerializer):
    """
    Facebook Url Сериализатор
    """

    class Meta:
        model = FacebookUrl
        fields = '__all__'

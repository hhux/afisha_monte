from rest_framework import serializers

from .models import FacebookPost


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

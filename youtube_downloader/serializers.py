from .models import Guide, Jumbotron
from rest_framework import serializers


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ['stet_count', 'header', 'footer']


class JumbotronSerializer(serializers.ModelSerializer):
    class Jumbotron:
        model = Guide
        fields = ['title', 'description', 'description']
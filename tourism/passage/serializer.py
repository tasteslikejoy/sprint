from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'fam', 'name', 'otc']


class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['latitude', 'longitude', 'height']


class LevelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Levels
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ['urls', 'title']


class PassagesSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    coord = CoordinatesSerializer()
    lvl = LevelsSerializer()
    img = ImagesSerializer()

    class Meta:
        model = Passages
        fields = ['title', 'beauty_title', 'other_title', 'connect']










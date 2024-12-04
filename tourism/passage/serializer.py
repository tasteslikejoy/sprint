from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'fam', 'name', 'otc']

    def save(self, **kwargs):

        if self.is_valid():
            user = User.objects.filter(pk=self.validated_data.get('pk'))

        if user.exists():
            return user.first()
        else:
            new_user = User.objects.create(
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc')
            )
            return new_user



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
    add_time = serializers.DateTimeField(format='%d %m %Y %H:%M:%S', read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Passages
        fields = ['title', 'beauty_title', 'other_title', 'connect']

    def validate(self, data):

        if self.instance:
            user = self.instance.user
            data_user = data['user']
            validation_fields = [
                user.email == data_user['email'],
                user.phone == data_user['phone'],
                user.fam == data_user['fam'],
                user.name == data_user['name'],
                user.otc == data_user['otc']
            ]

            if data_user and not all(validation_fields):
                 raise serializers.ValidationError('Отклонено: Данные пользователя нельзя изменить.')
            return data








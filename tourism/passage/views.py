from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializer import UserSerializer, CoordinatesSerializer, LevelsSerializer, ImagesSerializer, PassagesSerializer
from .models import User, Coordinates, Levels, Passages, Images
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['API по работе с координатами'])
class CoordinatesView(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer


@extend_schema(tags=['API по работе с уровнями'])
class LevelsView(viewsets.ModelViewSet):
    queryset = Levels.objects.all()
    serializer_class = LevelsSerializer


@extend_schema(tags=['API по работе с картинками'])
class ImagesView(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


@extend_schema(tags=['API по работе с пользователями'])
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=['API по работе с перевалами'])
class PassagesView(viewsets.ModelViewSet):
    queryset = Passages.objects.all()
    serializer_class = PassagesSerializer
    http_method_names = ['get', 'post', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__email']

    @extend_schema(tags=['Создание'])
    def create(self, request, *args, **kwargs):
        serializer = PassagesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': None,
                    'id': serializer.data['id'],
                }
            )

        if status.HTTP_400_BAD_REQUEST:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Bad Request',
                    'id': None,
                }
            )

        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response(
                {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': 'Ошибка подключения к базе данных',
                    'id': None,
                }
            )

    @extend_schema(tags=['Изменение'])
    def partial_update(self, request, *args, **kwargs):
        passage = self.get_object()

        if passage.status == 'new':
            serializer = PassagesSerializer(passage, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': '1',
                        'message': 'Запись успешно изменена'
                    }
                )
            else:
                return Response(
                    {
                        'status': '0',
                        'message': serializer.errors
                    }
                )
        else:
            return Response(
                {
                    'status': '0',
                    'message': f'Отклонено! {passage.get_status_display()}'
                }
            )




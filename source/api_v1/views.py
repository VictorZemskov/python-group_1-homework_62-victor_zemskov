from webapp.models import Movie
from webapp.models import Category
from webapp.models import Hall
from webapp.models import Seat
from webapp.models import Show
from rest_framework import viewsets
from api_v1.serializers import MovieSerializer
from api_v1.serializers import CategorySerializer
from api_v1.serializers import HallSerializer
from api_v1.serializers import SeatSerializer
from api_v1.serializers import ShowSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.active().order_by('-release_date')
    serializer_class = MovieSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.active().order_by('pk')
    serializer_class = CategorySerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.active().order_by('pk')
    serializer_class = HallSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.active().order_by('pk')
    serializer_class = SeatSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.active().order_by('pk')
    serializer_class = ShowSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

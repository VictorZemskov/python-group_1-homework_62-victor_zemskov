from webapp.models import Movie
from webapp.models import Category
from webapp.models import Hall
from webapp.models import Seat
from webapp.models import Show
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:movie-detail')

    class Meta:
        model = Movie
        fields = ('url', 'id', 'name', 'category_name', 'description', 'poster', 'release_date', 'finish_date')

class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:category-detail')

    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'description')

class HallSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:hall-detail')

    class Meta:
        model = Hall
        fields = ('url', 'id', 'name')

class SeatSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:seat-detail')

    class Meta:
        model = Seat
        fields = ('url', 'id', 'hall_name', 'line', 'position')

class ShowSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:show-detail')

    class Meta:
        model = Show
        fields = ('url', 'id', 'movie_name', 'hall_name', 'start_date', 'finish_date', 'price')



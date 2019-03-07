from webapp.models import Movie, Category, Hall, Seat, Show, Book, Ticket, Discount
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:category-detail')

    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'description')

class InlineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class MovieCreateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:movie-detail')

    class Meta:
        model = Movie
        fields = ('url', 'id', 'name', 'category_name', 'description', 'poster', 'release_date', 'finish_date')

class MovieDisplaySerializer(MovieCreateSerializer):
    category_name = InlineCategorySerializer(many=True, read_only=True)



class HallSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:hall-detail')

    class Meta:
        model = Hall
        fields = ('url', 'id', 'name')


class SeatSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:seat-detail')
    hall_url = serializers.HyperlinkedRelatedField(view_name='api_v1:hall-detail', read_only=True, source='hall_name')

    class Meta:
        model = Seat
        fields = ('url', 'id', 'hall_name', 'hall_url', 'line', 'position')

class InlineSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ('id', 'line', 'position')


class ShowSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:show-detail')
    movie_url = serializers.HyperlinkedRelatedField(view_name='api_v1:movie-detail', read_only=True, source='movie_name')
    hall_url = serializers.HyperlinkedRelatedField(view_name='api_v1:hall-detail', read_only=True, source='hall_name')

    class Meta:
        model = Show
        fields = ('url', 'id', 'movie_name', 'movie_url', 'hall_name', 'hall_url', 'start_date', 'finish_date', 'price')


class BookCreateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:book-detail')
    show_url = serializers.HyperlinkedRelatedField(view_name='api_v1:show-detail', read_only=True, source='show')

    class Meta:
        model = Book
        fields = ('url', 'id', 'code', 'show', 'show_url', 'seats', 'status', 'created_at', 'updated_at')

class BookDisplaySerializer(BookCreateSerializer):
    seats = InlineSeatSerializer(many=True, read_only=True)


class DiscountSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:discount-detail')

    class Meta:
        model = Discount
        fields = ('url', 'id', 'name', 'amount', 'date_start', 'date_finish')


class TicketSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:ticket-detail')
    show_url = serializers.HyperlinkedRelatedField(view_name='api_v1:show-detail', read_only=True, source='show_id')
    seat_url = serializers.HyperlinkedRelatedField(view_name='api_v1:seat-detail', read_only=True, source='seat_id')
    discount_url = serializers.HyperlinkedRelatedField(view_name='api_v1:discount-detail', read_only=True, source='discount_id')

    class Meta:
        model = Ticket
        fields = ('url', 'id', 'show_id', 'show_url', 'seat_id', 'seat_url', 'discount_id', 'discount_url', 'recurrence')

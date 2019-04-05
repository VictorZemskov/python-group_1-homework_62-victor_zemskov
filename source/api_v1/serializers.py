from webapp.models import Movie, Category, Hall, Seat, Show, Book, Ticket, Discount
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

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
        fields = ('url', 'id', 'show', 'show_url', 'seats', 'status', 'created_at', 'updated_at')


class BookDisplaySerializer(BookCreateSerializer):
    seats = InlineSeatSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields =('code', 'url', 'id', 'show', 'show_url', 'seats', 'status', 'created_at', 'updated_at')


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


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email']


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    # validated_data - содержит все данные, пришедшие при запросе (уже проверенные на правильность заполнения)
    def update(self, instance, validated_data):

        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email = validated_data.get('email')

        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email']

class AuthTokenSerializer(serializers.Serializer):
    token = serializers.CharField(write_only=True)

    def validate_token(self, token):
        try:
            return Token.objects.get(key=token)
        except Token.DoesNotExist:
            raise ValidationError("Invalid credentials")


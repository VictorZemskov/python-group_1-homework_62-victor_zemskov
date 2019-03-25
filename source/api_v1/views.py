from webapp.models import Movie, Category, Hall, Seat, Show, Book, Ticket, Discount
from rest_framework import viewsets
from api_v1.serializers import MovieCreateSerializer, MovieDisplaySerializer, CategorySerializer, HallSerializer,\
    SeatSerializer, ShowSerializer, BookDisplaySerializer, BookCreateSerializer, TicketSerializer, DiscountSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'id': user.pk,
            'is_admin': user.is_superuser,
            'is_staff': user.is_staff
        })


class BaseViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.method in ["POST", "DELETE", "PUT", "PATCH"]:
            permissions.append(IsAuthenticated())
        return permissions


class MovieViewSet(BaseViewSet):
    queryset = Movie.objects.active().order_by('-release_date')
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('release_date',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDisplaySerializer
        else:
            return MovieCreateSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    # def get_queryset(self):
    #     queryset = self.queryset
    #     release_date = self.request.query_params.get('release_date', None)
    #     if release_date is not None:
    #         queryset = queryset.filter(release_date__gte=release_date).order_by('-release_date')
    #     return queryset

class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.active().order_by('pk')
    serializer_class = CategorySerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class HallViewSet(BaseViewSet):
    queryset = Hall.objects.active().order_by('pk')
    serializer_class = HallSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class SeatViewSet(BaseViewSet):
    queryset = Seat.objects.active().order_by('pk')
    serializer_class = SeatSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class ShowViewSet(BaseViewSet):
    queryset = Show.objects.active().order_by('pk')
    serializer_class = ShowSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    def get_queryset(self):
        queryset = self.queryset
        movie_name_id = self.request.query_params.get('movie_name_id', None)
        start_date = self.request.query_params.get('start_date', None)
        finish_date = self.request.query_params.get('finish_date', None)
        hall_name_id = self.request.query_params.get('hall_name_id', None)
        if movie_name_id:
            queryset = queryset.filter(movie_name_id=movie_name_id)
        if start_date:
            queryset = queryset.filter(start_date__gte=start_date)
        if finish_date:
            queryset = queryset.filter(start_date__lte=finish_date)
        if hall_name_id:
            queryset = queryset.filter(hall_name_id=hall_name_id)
        return queryset

class BookViewSet(BaseViewSet):
    queryset = Book.objects.active().order_by('pk')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookDisplaySerializer
        else:
            return BookCreateSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class TicketViewSet(BaseViewSet):
    queryset = Ticket.objects.active().order_by('pk')
    serializer_class = TicketSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class DiscountViewSet(BaseViewSet):
    queryset = Discount.objects.active().order_by('pk')
    serializer_class = DiscountSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailView(viewsets.ModelViewSet):
    queryset = User.objects.all()

    model = User
    serializer_class = UserSerializer
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]


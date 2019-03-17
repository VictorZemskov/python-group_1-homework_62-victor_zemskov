from webapp.models import Movie, Category, Hall, Seat, Show, Book, Ticket, Discount
from rest_framework import viewsets
from api_v1.serializers import MovieCreateSerializer, MovieDisplaySerializer, CategorySerializer, HallSerializer,\
    SeatSerializer, ShowSerializer, BookDisplaySerializer, BookCreateSerializer, TicketSerializer, DiscountSerializer
# from django_filters.rest_framework import DjangoFilterBackend

class NoAuthModelViewSet(viewsets.ModelViewSet):
    authentication_classes = []

class MovieViewSet(viewsets.ModelViewSet):
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

    def get_queryset(self):
        queryset = self.queryset
        movie_name_id = self.request.query_params.get('movie_name_id', None)
        start_date = self.request.query_params.get('start_date', None)
        finish_date = self.request.query_params.get('finish_date', None)
        if movie_name_id:
            queryset = queryset.filter(movie_name_id=movie_name_id)
        if start_date:
            queryset = queryset.filter(start_date__gte=start_date)
        if finish_date:
            queryset = queryset.filter(finish_date__lte=finish_date)
        return queryset

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.active().order_by('pk')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookDisplaySerializer
        else:
            return BookCreateSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.active().order_by('pk')
    serializer_class = TicketSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.active().order_by('pk')
    serializer_class = DiscountSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
from webapp.models import Movie, Category, Hall, Seat, Show, Book, Ticket, Discount
from rest_framework import viewsets
from api_v1.serializers import MovieCreateSerializer, MovieDisplaySerializer, CategorySerializer, HallSerializer,\
    SeatSerializer, ShowSerializer, BookDisplaySerializer, BookCreateSerializer, TicketSerializer, DiscountSerializer

class NoAuthModelViewSet(viewsets.ModelViewSet):
    authentication_classes = []

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.active().order_by('-release_date')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDisplaySerializer
        else:
            return MovieCreateSerializer

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
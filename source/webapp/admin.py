from django.contrib import admin
from webapp.models import Movie, Category, Hall, Seat, Show, Book, Ticket, Discount

class MovieAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'release_date']
    ordering = ['-release_date']
    search_fields = ['name', 'id']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    ordering = ['pk']
    search_fields = ['name', 'id']

class HallAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    ordering = ['pk']
    search_fields = ['name', 'id']

class SeatAdmin(admin.ModelAdmin):
    list_display = ['pk', 'hall_name', 'line', 'position']
    ordering = ['pk']
    search_fields = ['position', 'id']

class ShowAdmin(admin.ModelAdmin):
    list_display = ['pk', 'movie_name', 'hall_name', 'start_date', 'finish_date', 'price']
    ordering = ['start_date']
    search_fields = ['movie_name', 'id']

class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'show', 'code', 'get_seats_display', 'status', 'created_at', 'updated_at']
    ordering = ['pk']
    search_fields = ['show', 'id']

class TicketAdmin(admin.ModelAdmin):
    list_display = ['pk', 'show_id', 'seat_id', 'discount_id', 'recurrence']
    ordering = ['pk']
    search_fields = ['show_id', 'id']

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'amount', 'date_start', 'date_finish']
    ordering = ['pk']
    search_fields = ['name', 'id']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Discount, DiscountAdmin)



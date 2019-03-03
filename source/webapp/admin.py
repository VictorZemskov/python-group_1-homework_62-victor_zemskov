from django.contrib import admin
from webapp.models import Movie
from webapp.models import Category
from webapp.models import Hall
from webapp.models import Seat
from webapp.models import Show

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
    list_display = ['pk', 'position']
    ordering = ['pk']
    search_fields = ['position', 'id']

class ShowAdmin(admin.ModelAdmin):
    list_display = ['pk', 'movie_name']
    ordering = ['pk']
    search_fields = ['movie_name', 'id']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Show, ShowAdmin)



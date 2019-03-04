from django.db import models
from django.urls import reverse

class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)

class Movie(models.Model):
    name = models.CharField(max_length=255)
    category_name = models.ManyToManyField('Category', null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)
    release_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:movie-detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:category-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Hall(models.Model):
    name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:hall-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Seat(models.Model):
    hall_name = models.ForeignKey(Hall, on_delete=models.PROTECT)
    line = models.IntegerField(max_length=2)
    position = models.IntegerField(max_length=2)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:seat-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Seat'

class Show(models.Model):
    movie_name = models.ForeignKey(Movie, on_delete=models.PROTECT)
    hall_name = models.ForeignKey(Hall, on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:show-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Show'
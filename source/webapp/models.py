from django.db import models
from django.urls import reverse
import random
import string
from django.conf import settings

class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)

class Movie(models.Model):
    name = models.CharField(max_length=255)
    category_name = models.ManyToManyField('Category', blank=True, related_name='categories')
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
    hall_name = models.ForeignKey(Hall, related_name='seats', on_delete=models.PROTECT)
    line = models.CharField(max_length=10)
    position = models.CharField(max_length=5)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:seat-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Line %s Position %s' % (self.line, self.position)

class Show(models.Model):
    movie_name = models.ForeignKey(Movie, related_name='shows', on_delete=models.PROTECT)
    hall_name = models.ForeignKey(Hall, related_name='shows', on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:show-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s, %s (%s - %s)" % (self.movie_name, self.hall_name,
                                     self.start_date.strftime('%d.%m.%Y %H:%M'),
                                     self.finish_date.strftime('%d.%m.%Y %H:%M'))


def generate_code():
    code = ""
    for i in range(0, settings.BOOKING_CODE_LENGHT):
        code += random.choice(string.digits)
    return code

BOOKING_STATUS_CHOICES = [
    ('created', 'Created'),
    ('sold', 'Sold'),
    ('canceled', 'Canceled'),
]

class Book(models.Model):
    code = models.CharField(max_length=12, unique_for_date='created_at', default=generate_code, editable=False)
    show = models.ForeignKey(Show, on_delete=models.PROTECT, related_name='booking')
    seats = models.ManyToManyField(Seat, related_name='booking')
    status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, default='created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return "%s %s" % (self.show, self.code)

    def get_seats_display(self):
        seats = ""
        for seat in self.seats.all():
            seats += "L%sP%s " % (seat.line, seat.position)
        return seats

class Discount(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_start = models.DateTimeField(null=True)
    date_finish = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:ticket-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s %s' % (self.name, self.amount)

class Ticket(models.Model):
    show_id = models.ForeignKey(Show, related_name='tickets', on_delete=models.PROTECT)
    seat_id = models.ForeignKey(Seat, related_name='tickets', on_delete=models.PROTECT)
    discount_id = models.ForeignKey(Discount, related_name='tickets', on_delete=models.PROTECT)
    recurrence = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:ticket-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s %s' % (self.show_id, self.seat_id)

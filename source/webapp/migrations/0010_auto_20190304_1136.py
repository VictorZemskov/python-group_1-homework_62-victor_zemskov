# Generated by Django 2.1 on 2019-03-04 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_movie_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category_name',
        ),
        migrations.AddField(
            model_name='movie',
            name='category_name',
            field=models.ManyToManyField(to='webapp.Category'),
        ),
    ]
# Generated by Django 2.1 on 2019-03-07 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20190307_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category_name',
            field=models.ManyToManyField(blank=True, related_name='categories', to='webapp.Category'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='hall_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='seats', to='webapp.Hall'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='line',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='seat',
            name='position',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='show',
            name='hall_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shows', to='webapp.Hall'),
        ),
        migrations.AlterField(
            model_name='show',
            name='movie_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shows', to='webapp.Movie'),
        ),
    ]

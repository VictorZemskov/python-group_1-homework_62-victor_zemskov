# Generated by Django 2.1 on 2019-03-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20190307_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

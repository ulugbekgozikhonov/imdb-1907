# Generated by Django 5.1.4 on 2024-12-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_watchlist_rating_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='rating_sum',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
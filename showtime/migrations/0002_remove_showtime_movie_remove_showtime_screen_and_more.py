# Generated by Django 5.1 on 2024-09-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtime', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtime',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='showtime',
            name='screen',
        ),
        migrations.RemoveField(
            model_name='showtime',
            name='theatre_id',
        ),
        migrations.AddField(
            model_name='showtime',
            name='movie_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='showtime',
            name='screen_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

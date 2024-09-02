# Generated by Django 5.1 on 2024-09-02 14:32

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0002_movie_duration'),
        ('screen', '0001_initial'),
        ('showtime', '0003_delete_showtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('theatre_id', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screen.screen')),
            ],
        ),
    ]

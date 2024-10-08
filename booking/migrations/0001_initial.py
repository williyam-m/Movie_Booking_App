# Generated by Django 5.1 on 2024-09-12 12:11

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('showtime', '0006_showtime_theatre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('seats', models.JSONField(default=list)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking_datetime', models.DateTimeField(auto_now_add=True)),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showtime.showtime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

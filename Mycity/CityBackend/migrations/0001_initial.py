# Generated by Django 3.2.5 on 2022-05-17 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('name', models.CharField(max_length=120)),
                ('category', models.CharField(choices=[('1', 'Disabled'), ('2', 'NotDisabled')], default=1, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Packing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingdate', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parkinginfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CityBackend.parkinginfo')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CityBackend.place')),
            ],
        ),
    ]
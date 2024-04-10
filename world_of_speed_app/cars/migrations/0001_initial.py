# Generated by Django 5.0.4 on 2024-04-06 13:56

import django.core.validators
import django.db.models.deletion
import world_of_speed_app.cars.valdiators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Rally', 'Rally'), ('Open-wheel', 'Open-wheel'), ('Kart', 'Kart'), ('Drag', 'Drag'), ('Other', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(1)])),
                ('year', models.IntegerField(validators=[world_of_speed_app.cars.valdiators.year_validator])),
                ('image_url', models.URLField(error_messages={'unique': 'This image URL is already in use! Provide a new one.'}, unique=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]

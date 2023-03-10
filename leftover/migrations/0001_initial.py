# Generated by Django 4.1.7 on 2023-03-07 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('listing_date', models.DateField(auto_now_add=True)),
                ('img', models.URLField()),
                ('ingredients', models.CharField(max_length=500)),
                ('allergens', models.CharField(max_length=500)),
                ('good_for_x_days', models.PositiveIntegerField()),
                ('num_servings', models.PositiveIntegerField()),
                ('pickup_by_time', models.DateTimeField()),
                ('is_expired', models.BooleanField(default=False)),
                ('is_out_of_food', models.BooleanField(default=False)),
            ],
        ),
    ]

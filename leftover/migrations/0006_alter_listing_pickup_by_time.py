# Generated by Django 4.1.7 on 2023-03-07 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leftover', '0005_alter_listing_pickup_by_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='pickup_by_time',
            field=models.DateTimeField(),
        ),
    ]

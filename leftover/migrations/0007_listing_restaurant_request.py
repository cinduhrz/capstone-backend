# Generated by Django 4.1.7 on 2023-03-09 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leftover', '0006_alter_listing_pickup_by_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='restaurant',
            field=models.CharField(default="Cindy's Restaurant", max_length=30),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('is_org', models.BooleanField()),
                ('num_servings', models.PositiveIntegerField()),
                ('status', models.CharField(default='pending', max_length=10)),
                ('listing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leftover.listing')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_property_on_sale_id_photo_back_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_for_renting',
            name='pin_location',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

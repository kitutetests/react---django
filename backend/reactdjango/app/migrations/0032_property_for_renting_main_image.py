# Generated by Django 5.0.3 on 2024-03-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_remove_property_for_renting_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_for_renting',
            name='main_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

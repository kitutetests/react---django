# Generated by Django 5.0.2 on 2024-03-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_on_sale',
            name='id_photo_back',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='property_on_sale',
            name='id_photo_front',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

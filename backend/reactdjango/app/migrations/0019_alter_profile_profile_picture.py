# Generated by Django 5.0.2 on 2024-03-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/default dp.jpg', null=True, upload_to='images/'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_rentalsubscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalsubscription',
            name='phone_number',
            field=models.CharField(max_length=13, null=True),
        ),
    ]

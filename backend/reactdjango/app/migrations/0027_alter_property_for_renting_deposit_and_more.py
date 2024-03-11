# Generated by Django 5.0.3 on 2024-03-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_property_for_renting_pin_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_for_renting',
            name='deposit',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='property_for_renting',
            name='garbage_fee',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='property_for_renting',
            name='water_fee',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

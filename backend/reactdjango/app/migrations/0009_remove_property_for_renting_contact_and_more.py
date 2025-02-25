# Generated by Django 5.0.2 on 2024-03-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_house_type_property_for_renting_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property_for_renting',
            name='contact',
        ),
        migrations.AddField(
            model_name='property_for_renting',
            name='agent_contact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property_for_renting',
            name='agent_name',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='property_for_renting',
            name='apartment_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='property_for_renting',
            name='caretaker_contact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property_for_renting',
            name='deposit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property_for_renting',
            name='garbage_fee',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property_for_renting',
            name='landlord_contact',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property_for_renting',
            name='water_fee',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property_for_renting',
            name='size',
            field=models.CharField(choices=[('single room', 'single room'), ('Double room', 'Double room'), ('Bedsitter', 'Bedsitter'), ('1 Bedroom', '1 Bedroom'), ('2 Bedrooms', '2 Bedrooms'), ('3 Bedrooms', '3 Bedrooms'), ('4 Bedrooms', '4 Bedrooms'), ('5 Bedrooms', '5 Bedrooms'), ('Above 6 Bedrooms', 'Above 6 Bedrooms')], max_length=50),
        ),
        migrations.AlterField(
            model_name='property_for_renting',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]

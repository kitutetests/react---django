# Generated by Django 5.0.2 on 2024-03-01 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1000)),
                ('size', models.CharField(choices=[('single room', 'single room'), ('Double room', 'Double room'), ('Bedsitter', 'Bedsitter'), ('1 Bedroom', '1 Bedroom'), ('2 Bedroom', '2 Bedroom'), ('3 Bedroom', '3 Bedroom'), ('Above 3 Bedroom', 'Above 3 Bedroom')], max_length=50)),
                ('features', models.TextField()),
                ('price', models.IntegerField()),
                ('contact', models.CharField(max_length=20)),
                ('posted', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
    ]

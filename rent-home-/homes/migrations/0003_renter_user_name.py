# Generated by Django 5.0.4 on 2024-05-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0002_home_phone_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='renter',
            name='user_name',
            field=models.CharField(default=0, max_length=100),
        ),
    ]

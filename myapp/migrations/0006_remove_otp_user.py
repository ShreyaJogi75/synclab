# Generated by Django 5.0.1 on 2024-08-31 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='user',
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-01 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpentry_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='description',
        ),
    ]

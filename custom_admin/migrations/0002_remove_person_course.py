# Generated by Django 4.2.6 on 2023-10-12 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='course',
        ),
    ]
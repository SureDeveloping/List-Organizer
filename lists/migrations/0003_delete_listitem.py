# Generated by Django 4.2.13 on 2024-05-20 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_listitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ListItem',
        ),
    ]
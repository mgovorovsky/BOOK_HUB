# Generated by Django 4.2.5 on 2023-10-12 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0006_alter_currency_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Currency',
        ),
    ]

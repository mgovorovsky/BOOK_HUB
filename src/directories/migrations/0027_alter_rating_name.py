# Generated by Django 4.2.5 on 2023-10-26 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0026_alter_rating_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='name',
            field=models.IntegerField(unique=True, verbose_name='Rating value'),
        ),
    ]

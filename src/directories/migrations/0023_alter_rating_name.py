# Generated by Django 4.2.5 on 2023-10-26 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0022_bookname_rating_alter_rating_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='name',
            field=models.CharField(max_length=3, unique=True, verbose_name='Rating value'),
        ),
    ]

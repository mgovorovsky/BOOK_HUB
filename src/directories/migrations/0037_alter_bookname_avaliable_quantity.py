# Generated by Django 4.2.5 on 2023-11-07 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0036_bookname_avaliable_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookname',
            name='avaliable_quantity',
            field=models.PositiveIntegerField(default=10, verbose_name='Quantity'),
        ),
    ]

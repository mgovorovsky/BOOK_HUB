# Generated by Django 4.2.5 on 2023-10-23 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0019_bookname_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookname',
            name='cover',
            field=models.ImageField(default=1, upload_to='order_images/%Y/%m/%d', verbose_name='Order Cover'),
        ),
    ]
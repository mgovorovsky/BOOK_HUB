# Generated by Django 4.2.5 on 2023-10-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cover',
            field=models.ImageField(default='-', upload_to='order_images/%Y/%m/%d', verbose_name='Order Cover'),
            preserve_default=False,
        ),
    ]

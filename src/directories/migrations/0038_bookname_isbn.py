# Generated by Django 4.2.5 on 2023-11-07 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0037_alter_bookname_avaliable_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookname',
            name='ISBN',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ISBN'),
        ),
    ]

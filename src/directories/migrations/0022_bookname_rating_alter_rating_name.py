# Generated by Django 4.2.5 on 2023-10-26 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0021_bookname_book_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookname',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book_names', to='directories.rating', verbose_name='Rating value'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='name',
            field=models.IntegerField(unique=True, verbose_name='Rating value'),
        ),
    ]

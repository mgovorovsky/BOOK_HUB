# Generated by Django 4.2.5 on 2023-10-08 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0004_copyrightholder_genre_alter_booktype_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookname',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_names', to='directories.author', verbose_name="Author's name"),
        ),
    ]

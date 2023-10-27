# Generated by Django 4.2.5 on 2023-10-27 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0031_remove_bookname_book_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookname',
            name='typebook',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='book_names', to='directories.booktype', verbose_name='Book type name'),
            preserve_default=False,
        ),
    ]

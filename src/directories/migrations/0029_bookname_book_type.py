# Generated by Django 4.2.5 on 2023-10-26 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0028_remove_bookname_booktypename'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookname',
            name='book_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book_names', to='directories.booktype', verbose_name='Book type name'),
        ),
    ]

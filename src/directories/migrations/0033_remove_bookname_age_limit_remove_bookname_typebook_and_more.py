# Generated by Django 4.2.5 on 2023-10-27 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0032_bookname_typebook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookname',
            name='age_limit',
        ),
        migrations.RemoveField(
            model_name='bookname',
            name='typebook',
        ),
        migrations.AddField(
            model_name='bookname',
            name='booktypename',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book_names', to='directories.booktype', verbose_name='Book type name'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='name',
            field=models.CharField(max_length=3, unique=True, verbose_name='Rating value'),
        ),
    ]

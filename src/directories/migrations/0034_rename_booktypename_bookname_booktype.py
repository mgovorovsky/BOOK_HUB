# Generated by Django 4.2.5 on 2023-10-27 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0033_remove_bookname_age_limit_remove_bookname_typebook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookname',
            old_name='booktypename',
            new_name='booktype',
        ),
    ]

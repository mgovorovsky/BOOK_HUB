# Generated by Django 4.2.5 on 2023-10-01 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('random_number', '0002_region_alter_author_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Book's name")),
                ('description', models.TextField(blank=True, null=True, verbose_name="Book's description")),
            ],
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
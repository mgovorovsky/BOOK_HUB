# Generated by Django 4.2.5 on 2023-10-01 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Author's name")),
                ('description', models.TextField(blank=True, null=True, verbose_name="Autor's deskription")),
            ],
        ),
    ]

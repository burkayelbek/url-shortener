# Generated by Django 4.1 on 2022-08-14 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortener',
            options={'ordering': ['-created'], 'verbose_name': 'Shortener', 'verbose_name_plural': 'Shorteners'},
        ),
        migrations.AlterModelTable(
            name='shortener',
            table='shortener',
        ),
    ]

# Generated by Django 4.0.1 on 2022-12-22 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_randevumodel_servisneden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='karavanmodel',
            name='agirlik',
        ),
        migrations.RemoveField(
            model_name='karavanmodel',
            name='disgenislik',
        ),
        migrations.RemoveField(
            model_name='karavanmodel',
            name='disyukseklik',
        ),
        migrations.RemoveField(
            model_name='karavanmodel',
            name='icgenislik',
        ),
        migrations.RemoveField(
            model_name='karavanmodel',
            name='icyukseklik',
        ),
        migrations.RemoveField(
            model_name='karavanmodel',
            name='kapasite',
        ),
    ]

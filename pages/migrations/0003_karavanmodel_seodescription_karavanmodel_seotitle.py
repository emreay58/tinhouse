# Generated by Django 4.1.3 on 2022-11-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_karavanmodel_img1_alter_karavanmodel_img10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='karavanmodel',
            name='seodescription',
            field=models.CharField(default='Tiny House İmalatı ve Modelleri, Star Tiny House sizlerle - Dilediğiniz modeller son teknoloji ürünler', max_length=165, verbose_name='Seo Description'),
        ),
        migrations.AddField(
            model_name='karavanmodel',
            name='seotitle',
            field=models.CharField(default='Tiny House İmalatı ve Modelleri - Star Tiny House Hizmetinizde', max_length=70, verbose_name='Seo Title'),
        ),
    ]

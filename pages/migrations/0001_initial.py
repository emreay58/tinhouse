# Generated by Django 4.0.1 on 2022-11-06 12:05

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kategori Girin')),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='KaravanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='modeller', verbose_name='Ana Ekran Resmi')),
                ('title', models.CharField(max_length=200, verbose_name='Ürün Başlığı')),
                ('description', models.TextField(verbose_name='Ön Açıklama')),
                ('description1', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Tam Açıklama')),
                ('agirlik', models.IntegerField(verbose_name='Ağırlık')),
                ('disyukseklik', models.IntegerField(verbose_name='Dış Yükseklik')),
                ('icyukseklik', models.IntegerField(verbose_name='İç Yükseklik')),
                ('disgenislik', models.IntegerField(verbose_name='Dış Genişlik')),
                ('icgenislik', models.IntegerField(verbose_name='İç Genişlik')),
                ('kapasite', models.IntegerField(verbose_name='Kapasite')),
                ('img1', models.ImageField(upload_to='modeller', verbose_name='Karavan Resmi Ekle')),
                ('img2', models.ImageField(upload_to='modeller', verbose_name='Karavan Resmi Ekle')),
                ('img3', models.ImageField(upload_to='modeller', verbose_name='Karavan Resmi Ekle')),
                ('img4', models.ImageField(upload_to='modeller', verbose_name='Karavan Resmi Ekle')),
                ('img5', models.ImageField(upload_to='modeller', verbose_name='Karavan Resmi Ekle')),
                ('img6', models.ImageField(upload_to='modeller', verbose_name='Karavan Resmi Ekle')),
                ('img7', models.ImageField(upload_to='modeller', verbose_name='Karavan Resmi Ekle')),
                ('img8', models.ImageField(upload_to='modeller', verbose_name='Karavan Resmi Ekle')),
                ('img9', models.ImageField(upload_to='modeller', verbose_name='Karavan Resmi Ekle')),
                ('img10', models.ImageField(upload_to='modeller', verbose_name='Karavan Resmi Ekle')),
                ('is_home', models.BooleanField(verbose_name='Ana Sayfada Gösterilsin Mi?')),
                ('is_active', models.BooleanField(verbose_name='Karavan Mevut Mu?')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.category', verbose_name='Kategori')),
            ],
        ),
    ]

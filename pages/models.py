from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kategori Girin')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name
    

class KaravanModel(models.Model):
    img = models.ImageField(upload_to='modeller', verbose_name='Ana Ekran Resmi')
    title = models.CharField(max_length=200, verbose_name='Ürün Başlığı')
    seotitle = models.CharField(max_length=70, verbose_name='Seo Title', default='Tiny House İmalatı ve Modelleri - Star Tiny House Hizmetinizde')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "Kategori")
    description = models.TextField(verbose_name='Ön Açıklama')
    seodescription = models.CharField(max_length=165, verbose_name='Seo Description', default="Tiny House İmalatı ve Modelleri, Star Tiny House sizlerle - Dilediğiniz modeller son teknoloji ürünler")
    description1 = RichTextUploadingField (verbose_name= 'Tam Açıklama')
    img1 = models.ImageField(upload_to="modeller", blank=True, verbose_name="Karavan Resmi Ekle")
    img2 = models.ImageField(upload_to="modeller", blank=True, verbose_name="Karavan Resmi Ekle")
    img3 = models.ImageField(upload_to="modeller", blank=True, verbose_name="Karavan Resmi Ekle")
    img4 = models.ImageField(upload_to="modeller", blank=True, verbose_name="Karavan Resmi Ekle")
    img5 = models.ImageField(upload_to="modeller", blank=True, verbose_name="Karavan Resmi Ekle")
    img6 = models.ImageField(upload_to="modeller", blank=True, verbose_name="Karavan Resmi Ekle")
    img7 = models.ImageField(upload_to="modeller", blank=True, verbose_name="Karavan Resmi Ekle")
    img8 = models.ImageField(upload_to="modeller", blank=True, verbose_name="Karavan Resmi Ekle")
    img9 = models.ImageField(upload_to="modeller", blank=True, verbose_name="Karavan Resmi Ekle")
    img10 = models.ImageField(upload_to="modeller", blank=True, verbose_name="Karavan Resmi Ekle")
    is_home = models.BooleanField(verbose_name='Ana Sayfada Gösterilsin Mi?')
    is_active = models.BooleanField(verbose_name = 'Karavan Mevut Mu?')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title

class RandevuModel(models.Model):
    name = models.CharField(max_length=200, verbose_name="Adı Soyadı")
    email = models.EmailField(verbose_name="E-Mail ")
    telefon = models.IntegerField(verbose_name="Telefon mumarası")
    konu = models.CharField(max_length=150, verbose_name="Konu")
    mesaj = models.TextField(verbose_name="Mesajınız")

    def __str__(self):
        return self.name

class YorumModel(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='yorum')
    yorum = models.TextField()
    unvan = models.CharField(max_length=50)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name
    
 
    








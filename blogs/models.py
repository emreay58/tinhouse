from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Başlık Ekle')
    img = models.ImageField(upload_to='blogs', verbose_name='Resim Ekle')
    description = models.TextField(verbose_name='Kısa Açıklama')
    description1 = RichTextUploadingField(verbose_name='Makele Detayı Yazın')
    date = models.DateField(auto_now_add=True)  
    slug = models.SlugField(unique=True, null=True)
    
    def __str__(self):
        return self.title
    

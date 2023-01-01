from django.contrib import admin
from . models import KaravanModel, Category, RandevuModel, YorumModel

# Register your models here.
@admin.register(KaravanModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description',)
    prepopulated_fields={'slug':('title',)}

@admin.register(Category)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields={'slug':('name',)}


@admin.register(RandevuModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('name',)
   
from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView, name='index'),
    path('hakkimizda/', views.AboutView, name='about'),
    path('iletisim/', views.ContactView, name='contact'),
    path('modeller/', views.ModelView, name='model'),
    path('modeller/<slug:slug>/', views.ModelDetailView, name='model_detail'),
    path('kategori/<slug:category_slug>/', views.CategoryView, name='category'),
    path('randevu/', views.RandevuView, name='randevu')
]

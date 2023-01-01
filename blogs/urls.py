from django.urls import path
from . import views

urlpatterns = [
    path ('', views.BlogView, name='blogs'),
    path ('<slug:slug>/', views.Blog_Detail_View, name='blog_detail')
]

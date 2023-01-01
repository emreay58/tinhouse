from django.shortcuts import render
from .models import BlogModel

# Create your views here.

def BlogView(request):
    blogs = BlogModel.objects.all()

    context = {
        'blogs' : blogs
    }
    return render(request, 'blogs/blogs.html', context)

def Blog_Detail_View(request, slug):
    blog = BlogModel.objects.get(slug=slug)

    context = {
        'blog' : blog
    }

    return render(request, 'blogs/blog_detail.html', context)

from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Blog, SubBlog

def home(request):
    blogs = Blog.objects.order_by('-id')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(blogs, 1)
    page_obj = paginator.page(page_num)
    ctx = {
        'object_list': page_obj,
        'latest_blog': blogs[:3]
    }

    return render(request, 'main/index.html', ctx)


def about(request):
    blogs = Blog.objects.order_by('-id')
    ctx = {
        'latest_blog': blogs[:4]
    }

    return render(request, 'main/about.html', ctx)
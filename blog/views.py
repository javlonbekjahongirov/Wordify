from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, Category, Tag


def blog_list(request):
    blogs = Blog.objects.all().order_by('-id')
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if q:
        blogs = blogs.filter(title__icontains=q)
    if cat:
        blogs = blogs.filter(category__title__exact=cat)
    if tag:
        blogs = blogs.filter(tags__title__exact=tag)
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        'object_list': page_obj,
    }
    return render(request, 'main/index.html', ctx)


def blog_detail(request, **kwargs):
    slug = kwargs.get('slug', None)
    year = kwargs.get('year', None)
    month = kwargs.get('month', None)
    day = kwargs.get('day', None)
    obj = get_object_or_404(Blog, created_date__year=year,created_date__month=month, created_date__day=day, slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    related_posts = Blog.objects.order_by('-id')[:3]
    ctx = {
        'object': obj,
        'categories': categories,
        'tags': tags,
        'related_posts': related_posts[:3]

    }

    return render(request, 'blog/blog-single.html', ctx)


def blog_category(request):

    return render(request, 'category.html')

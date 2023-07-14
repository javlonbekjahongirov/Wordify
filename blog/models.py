from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify

from profiles.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    title = models.CharField(max_length=221)
    slug = models.SlugField(null=True, blank=True, unique_for_date='created_date', max_length=221)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    views = models.IntegerField(default=0, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        url = reverse('blog:detail', kwargs={
            "year": self.created_date.year,
            "month": self.created_date.month,
            "day": self.created_date.day,
            "slug": self.slug
        })

        return url


# class BlogTag(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class SubBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=221)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.blog.title


def blog_pre_save(instance, sender, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    return instance


pre_save.connect(blog_pre_save, sender=Blog)

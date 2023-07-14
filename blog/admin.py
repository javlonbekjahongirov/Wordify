from django.contrib import admin
from .models import Category, Tag, Blog, SubBlog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


class SubBlogInline(admin.StackedInline):
    model = SubBlog
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = (SubBlogInline, )
    list_display = ('id', 'author', 'title', 'category', 'views', 'created_date')
    search_fields = ('title', 'author__username', 'category__title')
    list_filter = ('created_date', )
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags', )


@admin.register(SubBlog)
class SubBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'title')
    search_fields = ('title', 'blog__title')



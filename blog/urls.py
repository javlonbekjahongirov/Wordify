from django.urls import path

from .views import blog_category, blog_detail, blog_list
from main.views import about

app_name = 'blog'

urlpatterns = [
    path('detail/<str:year>/<str:month>/<int:day>/<slug:slug>/', blog_detail, name='detail'),
    path('category', blog_category, name='category'),
    path('list', blog_list, name='list'),
    path('about', about, name='about')

]
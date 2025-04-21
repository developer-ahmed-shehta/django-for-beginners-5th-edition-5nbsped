from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='blog_home'),
    path('post/<int:postID>',post_detail,name='post_detail'),
]
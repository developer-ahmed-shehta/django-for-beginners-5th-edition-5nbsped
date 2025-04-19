from django.shortcuts import render
from django.views.generic import TemplateView,ListView

from MessageBoardWebsite.models import Post

# Create your views here.


class PostList(ListView):
    template_name = "MessageBoardWebsite/post_list.html"
    model = Post

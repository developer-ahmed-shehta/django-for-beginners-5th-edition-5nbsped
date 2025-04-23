from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Blog.models import Post
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request,"Blog/home.html",context)
#
# def post_detail(request, postID):
#     post = get_object_or_404(Post, pk=postID)
#     context = {'post': post}
#     return render(request,"Blog/post_detail.html",context)

class BlogListView(ListView):
    model = Post
    template_name = "Blog/home.html"
    context_object_name = "posts"
class BlogDetailView(DetailView):
    model = Post
    template_name = "Blog/post_detail.html"

class BlogCreateView(CreateView): # new
    model = Post
    template_name = "Blog/post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "Blog/post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "Blog/post_delete.html"
    success_url = reverse_lazy("blog_home")

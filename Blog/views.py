from django.shortcuts import render, get_object_or_404

from Blog.models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,"Blog/home.html",context)

def post_detail(request, postID):
    post = get_object_or_404(Post, pk=postID)
    context = {'post': post}
    return render(request,"Blog/post_detail.html",context)
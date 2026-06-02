from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content, author=request.user)
    return render(request, 'blog/post_create.html')

@login_required
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
    return render(request, 'blog/post_edit.html', {'post': post})


@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return render(request, 'blog/post_delete.html')
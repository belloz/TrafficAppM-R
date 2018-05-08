from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, "index.html", {})

@login_required
def post_ticket(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('traffic:post_detail', id=post.id) # ('post_detail', id=post.id)
        else:
            form = PostForm()
    return render(request, 'post_ticket.html', {'form': form})

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def post_detail(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_categories(request, category):
    post = Post.objects.filter(category = category).order_by('-published_date')
    return render(request, 'categories.html', {'post': post})

@login_required
def profile(request, id):
    user = User.objects.get(id = id)
    posts = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'user': user, 'posts': posts})

def help(request):
    return render(request, 'help.html', {})
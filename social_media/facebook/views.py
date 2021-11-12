from django.shortcuts import render
from .models import Post
from .forms import PostForm


def posts_list(request):

    user_posts = Post.objects.all().filter()

    context = {'user_posts':user_posts}

    return render(request,'facebook/user_posts.html',context)


def create_post(request):

    if request.method == 'POST':

        form = PostForm(data=request.POST)

        if form.is_valid():
            form.save()

    else:
        form = PostForm()
    return render(request,'facebook/create_post.html',{'form':form})


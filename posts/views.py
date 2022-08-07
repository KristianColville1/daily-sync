from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm


def get_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Your post has been deleted')
    return redirect('/feed/')


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('/feed/')
    form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'posts/edit_post.html', context)

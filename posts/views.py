from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm, CommentForm


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
            messages.add_message(request, messages.SUCCESS,
                                 'Your post has been edited')
        return redirect('/feed/')
    form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'posts/edit_post.html', context)


def create_comment(request, post_id):
    """
    Handles submitting posts and redirects
    back to the previous page.
    """
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.name = request.user.username
        comment_form.instance.email = request.user.email
        comment_form.instance.approved = True
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        messages.add_message(request, messages.SUCCESS,
                             'Your comment has been submitted')
    else:
        messages.add_message(
            request, messages.ERROR,
            'Oops something has went wrong, please try again!')
    return redirect(request.META.get('HTTP_REFERER'))

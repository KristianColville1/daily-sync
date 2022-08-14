from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm


# ...................................................... Creating
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
    return redirect(request.META.get('HTTP_REFERER', '/'))


def create_post(request):
    """
    Handles submitting posts and redirects
    back to the previous page.
    """
    form = PostForm(data=request.POST)
    if form.is_valid():
        form.instance.author = request.user
        form.instance.status = 1
        form.save()
        messages.add_message(request, messages.SUCCESS,
                             'Your post has been submitted')
    else:
        messages.add_message(
            request, messages.ERROR,
            'Oops something has went wrong, please try again!')
    return redirect(request.META.get('HTTP_REFERER', '/'))


# ...................................................... Editing
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


def edit_comment(request, comment_id):
    """
    Edits a comment for the user
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your comment has been edited')
        return redirect('/feed/')
    form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'posts/edit_comment.html', context)


# ...................................................... Deleting
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Your post has been deleted')
    return redirect('/feed/')


def delete_comment(request, comment_id):
    """
    Deletes a comment for the user
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Your comment has been deleted')
    return redirect(request.META.get('HTTP_REFERER', '/'))


# ...................................................... Likes
def like_post(request, post_id):
    """
    Allows a user to like and unlike a post
    """
    post = get_object_or_404(Post, id=post_id)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', '/'))


def like_comment(request, comment_id):
    """
    Allows a user to like and unlike a comment
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', '/'))

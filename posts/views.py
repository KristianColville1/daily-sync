from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from notifications.signals import notify
from .models import Post, Comment
from .forms import PostForm, CommentForm
from profiles.models import Profile


# ...................................................... Creating
def create_comment(request, post_id):
    """
    Handles submitting posts and redirects
    back to the previous page.
    """
    post = get_object_or_404(Post, id=post_id)
    their_profile = get_object_or_404(Profile, user=post.author)
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.name = request.user
        comment_form.instance.email = request.user.email
        comment_form.instance.approved = True
        comment = comment_form.save(commit=False)
        comment.post_name = post
        comment.save()
        messages.add_message(request, messages.SUCCESS,
                             'Your comment has been submitted')
        if request.user != their_profile:
            notify.send(sender=request.user,
                recipient=their_profile.user,
                verb=f'created a comment on your post')
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


def share_post(request, post_id):
    """
    Handles sharing posts and redirects
    back to the same page.
    """
    form = PostForm(data=request.POST)
    if form.is_valid():
        form.instance.author = request.user
        form.instance.status = 1
        form.instance.post_shared = get_object_or_404(Post, id=post_id)
        their_profile = get_object_or_404(
            Profile, user=form.instance.post_shared.author)
        form.instance.is_shared = True
        form.save()
        messages.add_message(request, messages.SUCCESS,
                             'Your post has been submitted')
        if request.user != their_profile:
            notify.send(sender=request.user,
                        recipient=their_profile.user,
                        verb=f'has shared your post')
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
    return redirect(request.META.get('HTTP_REFERER', '/'))


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
def like_post(request, post_id, emoji):
    """
    Allows user to pick an emoji to use on a post
    """
    post = get_object_or_404(Post, id=post_id)
    their_profile = get_object_or_404(Profile, user=post.author)
    emoji_dict = {
        'like': post.thumbs_likes,
        'love': post.heart_likes,
        'laugh': post.laugh_likes,
        'angry': post.angry_likes,
    }

    if post.total_likes.filter(id=request.user.id).exists():
        post.total_likes.remove(request.user)
        for key, value in emoji_dict.items():
            value.remove(request.user)
    else:
        post.total_likes.add(request.user)
        for key, value in emoji_dict.items():
            if key == str(emoji):
                value.add(request.user)
    if request.user != their_profile.user:
        notify.send(sender=request.user,
                        recipient=their_profile.user,
                        verb=f'liked your post')
    return redirect(request.META.get('HTTP_REFERER', '/'))


def like_comment(request, comment_id, emoji):
    """
    Allows user to pick an emoji to use on a comment
    """
    comment = get_object_or_404(Comment, id=comment_id)
    their_profile = get_object_or_404(Profile, user=comment.name)
    emoji_dict = {
        'like': comment.thumbs_likes,
        'love': comment.heart_likes,
        'laugh': comment.laugh_likes,
        'angry': comment.angry_likes,
    }

    if comment.total_likes.filter(id=request.user.id).exists():
        comment.total_likes.remove(request.user)
        for key, value in emoji_dict.items():
            value.remove(request.user)
    else:
        comment.total_likes.add(request.user)
        for key, value in emoji_dict.items():
            if key == str(emoji):
                value.add(request.user)
    if request.user != their_profile.user:
        notify.send(sender=request.user,
                        recipient=their_profile.user,
                        verb=f'liked your comment')
    return redirect(request.META.get('HTTP_REFERER', '/'))

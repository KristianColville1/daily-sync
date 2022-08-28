from django.contrib import admin
from django.contrib.auth.models import User, Group
from posts.models import Post, Comment
from .models import Profile


class PostInlineAdmin(admin.StackedInline):
    """
    PostInlineAdmin  class
    """
    model = Post
    list_display = ('author', 'post_body', 'slug', 'status', 'created_on',)
    search_fields = ['author', 'post_body', 'slug']


class CommentInlineAdmin(admin.StackedInline):
    """
    CommentInlineAdmin class
    """
    model = Comment
    list_display = ('name', 'content', 'slug', 'created_on',)
    search_fields = ['name', 'content', 'slug']


class ProfileInlineAdmin(admin.StackedInline):
    """
    ProfileInlineAdmin class
    """
    model = Profile
    list_display = ('first_name', 'last_name', 'email', 'slug',)
    search_fields = ['first_name', 'last_name', 'content', 'slug']


class UserAdmin(admin.ModelAdmin):
    """
    UserAdmin provides a better site owner experience to manage the various
    models that a user can create
    """
    model = User
    fields = ['username', 'email']
    inlines = [ProfileInlineAdmin, PostInlineAdmin, CommentInlineAdmin]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

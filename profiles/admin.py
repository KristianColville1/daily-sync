from django.contrib import admin
from django.contrib.auth.models import User, Group
from posts.models import Post, Comment
from .models import Profile


class PostInlineAdmin(admin.StackedInline):
    """
    PostInlineAdmin mixin to display posts in user inside admin panel.
    Provides a cleaner interface to work with. Uses Summernote to provide a
    better editor.
    """
    model = Post
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']


class CommentInlineAdmin(admin.StackedInline):
    """
    CommentInlineAdmin mixin to display posts in user inside admin panel.
    Provides a cleaner interface to work with. Uses Summernote to provide a
    better editor.
    """
    model = Comment
    list_display = ('content', 'created_on')
    search_fields = ['content']


class ProfileInlineAdmin(admin.StackedInline):
    """
    ProfileInlineAdmin class
    """
    model = Profile


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

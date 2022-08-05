from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('body')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('content', 'created_on')
    search_fields = ['content']
    summernote_fields = ('content',)

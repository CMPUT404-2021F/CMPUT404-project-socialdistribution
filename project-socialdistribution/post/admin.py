from django.contrib import admin

# Register your models here.
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)

class CommentInline(admin.StackedInline): 
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin): 
    inlines = [
        CommentInline,
    ]

from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from blog.models import Article

admin.site.register(Article, MarkdownModelAdmin)

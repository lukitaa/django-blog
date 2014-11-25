from django.contrib import admin
from blog.models import Article
from blog.forms import ArticleForm

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

admin.site.register(Article, ArticleAdmin)

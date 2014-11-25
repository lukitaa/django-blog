from django.shortcuts import render

from blog.models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-created')[:3]
    context = {
        'latest_article_list': latest_article_list,
    }
    return render(request, 'blog/index.html', context)

from django.http import Http404
from django.shortcuts import render, redirect

from blog.models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-created')[:3]
    context = {
        'latest_article_list': latest_article_list,
    }
    return render(request, 'blog/index.html', context)

def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        context = { 'article': article }
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'blog/detail.html', context)

def comment(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        # Create comment
        article.comment_set.create(
            text=request.POST['text'], 
            commenter=request.POST['commenter']
        )
    except Article.DoesNotExist:
        raise Http404

    return redirect(article)

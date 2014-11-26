from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from blog.models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-created')[:3]
    context = {
        'latest_article_list': latest_article_list,
    }
    return render(request, 'blog/index.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = { 'article': article }
    return render(request, 'blog/detail.html', context)

def comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # Create comment
    #TODO: catch exceptions
    article.comment_set.create(
        text=request.POST['text'], 
        commenter=request.POST['commenter']
    )

    return HttpResponseRedirect(reverse('blog:detail', args=[article.id]))

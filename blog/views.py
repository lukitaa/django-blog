from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from blog.models import Article


class IndexView(generic.ListView):
#    template_name = 'blog/index.html'

    def get_queryset(self):
        '''
        Return the last five articles.
        '''
        return Article.objects.order_by('-created')[:5]


class DetailView(generic.DetailView):
    model = Article


def comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # Create comment
    #TODO: catch exceptions
    article.comment_set.create(
        text=request.POST['text'], 
        commenter=request.POST['commenter']
    )

    return HttpResponseRedirect(reverse('blog:detail', args=[article.id]))

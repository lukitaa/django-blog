from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Article(models.Model):
    '''
    Attributes of a blog post
    '''

    title = models.CharField(
        max_length=100,
    )
    text = models.TextField(
        help_text='The text of the article (in Markdown).',
    )
    created = models.DateField(
        auto_now_add=True,
        help_text='Creation date of the article.',
    )
    modified = models.DateField(
        auto_now=True,
        help_text='Modification date of the article.',
    )
    author = models.ForeignKey(
        User,
        help_text='The author of the article.',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
#        return '/%i' % self.id
        return reverse('blog:detail', args=[self.id])

    class Meta:
        ordering = ('-created',)

class Comment(models.Model):
    '''
    A comment of an article
    '''

    text = models.TextField(
        help_text='The text of the comment.',
    )
    created = models.DateField(
        auto_now_add=True,
        help_text='Creation date of the comment.',
    )
    commenter = models.CharField(
        max_length=50,
        help_text='Author of the comment.'
    )
    article = models.ForeignKey(Article)

    def __str__(self):
        return 'By ' + self.commenter +  ' at ' + str(self.created)

    class Meta:
        ordering = ('-created',)

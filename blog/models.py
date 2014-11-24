from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    '''
    Attributes of a blog post
    '''

    title = models.CharField(max_length=100)
    text = models.TextField,
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    author = models.ForeignKey(
        User,
        help_text='The author of the article.',
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

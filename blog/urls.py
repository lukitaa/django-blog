from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    # ex: /blog/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /blog/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /blog/5/comment
    url(r'^(?P<article_id>\d+)/comment/$', views.comment, name="comment"),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yet_another_blog.views.home', name='home'),
    url(r'^', include('blog.urls')),
#    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include('django_markdown.urls')),
)

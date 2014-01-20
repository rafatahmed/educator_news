from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # My urls
    url(r'^', include('ed_news.urls', namespace='ed_news')),

    url(r'^admin/', include(admin.site.urls)),

    # Auth urls
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'ed_news.views.logout_view', name='logout_view'),
    url(r'^profile/', 'ed_news.views.profile', name='profile'),
    url(r'^password_change/', 'ed_news.views.password_change_form', name='password_change_form'),
    url(r'^password_change_successful/', 'ed_news.views.password_change_successful', name='password_change_successful'),
)

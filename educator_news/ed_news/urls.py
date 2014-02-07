from django.conf.urls import patterns, url

from ed_news import views

urlpatterns = patterns('',
    # My urls

    # --- Educator News home page ---
    url(r'^$', views.index, name='index'),

    url(r'^new/', views.new, name='new'),
    url(r'^submit/', views.submit, name='submit'),
    url(r'^upvote_article/(?P<article_id>\d+)/$', views.upvote_article, name='upvote_article'),
    url(r'^discuss/(?P<article_id>\d+)/$', views.discuss, name='discuss'),
    url(r'^upvote_comment/(?P<comment_id>\d+)/$', views.upvote_comment, name='upvote_comment'),
    url(r'^downvote_comment/(?P<comment_id>\d+)/$', views.downvote_comment, name='downvote_comment'),
    url(r'^reply/(?P<article_id>\d+)/(?P<comment_id>\d+)/$', views.reply, name='reply'),
    url(r'^flag_comment/(?P<article_id>\d+)/(?P<comment_id>\d+)/$', views.flag_comment, name='flag_comment'),

    # --- My admin pages ---
    #  All of these check for my username.
    #  Could this be faked?
    #   I don't think so; checks against user object, not just username.
    #   None should offer any actions, or private info, without verifying this.
    url(r'^discuss_admin/(?P<article_id>\d+)/$', views.discuss_admin, name='discuss_admin'),
)

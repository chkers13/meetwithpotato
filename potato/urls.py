# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:33:52 2019

@author: chkers
"""

from django.conf.urls import url
from potato.views import home_view,PostDetailView,post_user,like_json,login_view,get_post,post_create
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', home_view, name='home_view'),
    url(r'^post/(?P<pk>\d+)$', get_post, name='post-detail'),
    url(r'^like_json$',views.like_json),
   	url(r'^postcreate$', post_create, name='post-create'),
    #url(r'^post/(?P<pk>\d+)$', PostDetailView.get_comment(), name='post_detail'),
    url(r'^(?P<author>\w+)$', post_user, name='userpost'),
    
    
  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
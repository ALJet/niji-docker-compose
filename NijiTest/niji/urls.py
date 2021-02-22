from django.conf.urls import url,include
from django.views.decorators.csrf import  csrf_exempt
from rest_framework import routers
from . import api
from . import views
from django.urls import path,re_path



api_router = routers.DefaultRouter()
api_router.register(r'topics',api.TopicApiView)
api_router.register(r'post',api.PostApiView)




urlpatterns = [
    re_path(r'^page/(?P<page>[0-9]+)/$', views.Index.as_view(), name='index'),
    re_path(r'^$', views.Index.as_view(), name='index'),
    re_path(r'^n/(?P<pk>\d+)/page/(?P<page>[0-9]+)/$', views.NodeView.as_view(), name='node'),
    re_path(r'^n/(?P<pk>\d+)/$', views.NodeView.as_view(), name='node'),
    re_path(r'^t/(?P<pk>\d+)/edit/$', views.edit_topic, name='edit_topic'),
    re_path(r'^t/(?P<pk>\d+)/append/$', views.create_appendix, name='create_appendix'),
    re_path(r'^t/(?P<pk>\d+)/page/(?P<page>[0-9]+)/$', views.TopicView.as_view(), name='topic'),
    re_path(r'^t/(?P<pk>\d+)/$', views.TopicView.as_view(), name='topic'),
    re_path(r'^u/(?P<pk>\d+)/$', views.user_info, name='user_info'),
    re_path(r'^u/(?P<pk>\d+)/topics/page/(?P<page>[0-9]+)/$', views.UserTopics.as_view(), name='user_topics'),
    re_path(r'^u/(?P<pk>\d+)/topics/$', views.UserTopics.as_view(), name='user_topics'),
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^reg/$', views.reg_view, name='reg'),
    re_path(r'^logout/$', views.logout_view, name="logout"),
    re_path(r'^search/$', views.search_redirect, name='search_redirect'),
    re_path(r'^search/(?P<keyword>.*?)/page/(?P<page>[0-9]+)/$', views.SearchView.as_view(), name='search'),
    re_path(r'^search/(?P<keyword>.*?)/$', views.SearchView.as_view(), name='search'),
    re_path(r'^t/create/$', views.create_topic, name='create_topic'),
    re_path(r'^notifications/$', views.NotificationView.as_view(), name='notifications'),
    re_path(r'^avatar/$', views.upload_avatar, name="upload_avatar"),
    re_path(r'^api/', include(api_router.urls)),
]



app_name = 'niji'



from django.conf.urls import include, url
from . import views

urlpatterns = [
#	url(r'^$', views.user_request_list, name='user_request_list'),
	url(r'^$', views.user_request_new, name='user_request_new'),
	url(r'^user_request/(?P<pk>[0-9]+)/$', views.user_request_detail, name='user_request_detail'),
	url(r'^user_request/new/$', views.user_request_new, name='user_request_new'),
	url(r'^user_request/(?P<pk>[0-9]+)/edit/$', views.user_request_edit, name='user_request_edit'),
	url(r'^user_request/list/$', views.user_request_list, name='user_request_list'),
	url(r'^user_request/(?P<pk>[0-9]+)/remove/$', views.user_request_remove, name='user_request_remove'),
#	url(r'^user_information/(?P<pk>[0-9]+)/$', views.user_information_detail, name='user_information_detail'),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
]

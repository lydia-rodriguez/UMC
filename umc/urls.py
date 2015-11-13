from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.user_request_list, name='user_request_list'),
	url(r'^user_request/(?P<pk>[0-9]+)/$', views.user_request_detail, name='user_request_detail'),
	url(r'^user_request/new/$', views.user_request_new, name='user_request_new'),
]

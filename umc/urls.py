from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_request_list, name='user_request_list'),
]

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.tenor_list, name='tenor_list'),
    url(r'^gif_send/$', views.gif_send, name='gif_send'),
]
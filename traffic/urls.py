from django.conf.urls import url
from . import views

app_name = "traffic"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^profile/(?P<id>\d+)/$', views.profile, name="profile"),
    url(r'^post_ticket/$', views.post_ticket, name="post_ticket"),
    url(r'^post_list/$', views.post_list, name="post_list"),
    url(r'^post_list/(?P<id>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^post_list/category/(?P<category>\w+)/$', views.post_categories, name="post_categories"),
    url(r'^help/$', views.help, name="help"),

    url(r'^tst/$', views.tst, name="tst"),
]

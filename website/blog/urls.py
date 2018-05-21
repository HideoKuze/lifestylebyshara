from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^landing', views.landing, name='landing'),
    url(r'^posts', views.blog, name='blog'),
    #url(r'^post/(?P<pk>\d+)_(?P<return_to_landing>\w+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.upload_image, name='upload_image'),

]


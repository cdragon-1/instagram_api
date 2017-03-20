from django.conf.urls import url

from .. import views


app_name = 'post'
urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post-list'),
    url(r'^(?P<pk>[0-9]+)/$,' views.PostDetail.as_viewa(), name='post-detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$,' views.PostDelete.as_viewa(), name='post-delete'),

    # url(r'^$', views.post_list, name='list'),
    # url(r'^create/$', views.post_create, name='post-create'),
    # url(r'^photo/add/$', views.post_photo_add, name='photo_add'),
]
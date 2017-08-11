from django.conf.urls import url
from . import views


app_name = 'sermons'

urlpatterns = [
    url(r'^$', views.IndexSermonView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.SermonDetailView.as_view(), name='detail'),
]

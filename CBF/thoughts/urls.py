from django.conf.urls import url

from . import views


app_name = 'thoughts'

urlpatterns = [
    url(r'^$', views.IndexThoughtView.as_view(), name="index"),
    url(r'^(?P<slug>[-\w]+)/$', views.ThoughtDetailView.as_view(), name="detail"),
]

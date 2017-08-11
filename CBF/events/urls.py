from django.conf.urls import url
from . import views


app_name = 'events'

urlpatterns = [
    url(r'^$', views.IndexEventView.as_view(), name="index"),
    url(r'^(?P<slug>[-\w]+)/$', views.EventDetailView.as_view(), name="detail"),
]

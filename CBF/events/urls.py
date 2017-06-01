from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexEventView.as_view(), name="event_index"),
    url(r'^(?P<slug>[-\w]+)/$', views.EventDetailView.as_view(), name="event_detail"),
]

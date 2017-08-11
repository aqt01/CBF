from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexThoughtView.as_view(), name="thought_index"),
    url(r'^(?P<slug>[-\w]+)/$', views.ThoughtDetailView.as_view(), name="thought_detail"),
]

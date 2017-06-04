from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexPreachView.as_view(), name="preach_index"),
    url(r'^(?P<slug>[-\w]+)/$', views.PreachDetailView.as_view(), name="preach_detail"),
]

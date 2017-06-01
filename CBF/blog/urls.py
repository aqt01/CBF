from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexMessageView.as_view(), name="blog_index"),
    url(r'^(?P<slug>[-\w]+)/$', views.MessageDetailView.as_view(), name="blog_detail"),
]

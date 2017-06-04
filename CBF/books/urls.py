from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BookIndexView.as_view(), name="book_index"),
    url(r'^(?P<slug>[-\w]+)/$', views.BookDetailView.as_view(), name="book_detail"),
]

from django.conf.urls import url
from . import views


app_name = 'home'

urlpatterns = [
    url(r'^$', views.IndexHomeView.as_view(), name='home'),
    url(r'^busqueda/', views.SearchResult.as_view(), name='search'),

]

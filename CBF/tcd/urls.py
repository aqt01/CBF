from django.conf.urls import include, url

from .views import TCDSubscriptionView, TCDSubscriptionViewThanks, TCDRegisterView

app_name = 'tcd'

urlpatterns = [

    url(
        regex=r'^$',
        view=TCDSubscriptionView.as_view(),
        name='subscription'
    ),
    url(
        regex=r'register/$',
        view=TCDRegisterView.as_view(),
        name='register'
    ),
    url(
        regex=r'gracias/$',
        view=TCDSubscriptionViewThanks.as_view(),
        name='thanks'
    ),




]

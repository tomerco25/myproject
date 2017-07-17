from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.category, name='hello'),
    url(r'^1/', views.category, name='hello'),
]
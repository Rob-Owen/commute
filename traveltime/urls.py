from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^search/', views.results, name='search'),
    url(r'$', views.input, name='index'),
]
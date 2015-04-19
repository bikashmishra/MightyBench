from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
	url(r'^(?P<hclass_id>\w+)/results/', views.results, name='results'),
	url(r'^index/', views.index, name='index'),
	url(r'^signup/', views.signup, name='signup'),
]
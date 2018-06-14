from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
	path('change-language', views.changeLanguage),
    url(r'^(?P<language>(en)|(fr))/submit(/?)$', views.submit),
	url(r'^(?P<language>(en)|(fr))(/?)$', views.form),
    path(r'', views.form, {'language': 'en'}),
]
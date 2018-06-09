from django.conf.urls import url
from . import views
from django.urls import path, re_path

urlpatterns = [
    re_path('/(?P<language>^en|fr$)/submit/', views.submit),
	re_path('/(?P<language>^en|fr$)/', views.form),
    path(r'', views.form, {'language': 'en'}),
]
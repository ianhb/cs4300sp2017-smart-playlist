from django.conf.urls import url

from smart_playlist import views

app_name = 'sp'
urlpatterns = [
    url(r'$', views.search, name="search"),
]
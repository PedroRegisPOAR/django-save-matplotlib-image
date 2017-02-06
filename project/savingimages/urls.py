from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^create_image_and_show', views.create_image_and_show, name="create_image_and_show"),
]
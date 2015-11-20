from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(.*)\.png$', views.render_image),
    url(r'^list.html$', views.getList)
]

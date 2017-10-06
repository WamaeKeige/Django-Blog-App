from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact , name='contact'),
    url(r'^downloads/$', views.downloads , name='downloads'),
    url(r'^services/$', views.services , name='services'),
    url(r'^about/$', views.about , name='about'),
    url(r'^portfolio/$', views.portfolio , name='portfolio'),

]    

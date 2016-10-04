from django.conf.urls import url
from .views import index, registrar, modificar, eliminar, buscar

urlpatterns = [
    url(r'^$', index.as_view(),name="index"),
    url(r'^registrar/$',registrar.as_view(),name="registro"),
    url(r'^actualizar/(?P<pk>[\w-]+)/$', modificar.as_view(),name="actualizar"),
    url(r'^eliminar/(?P<pk>[\w-]+)/$', eliminar.as_view(),name="eliminar"),
    url(r'^buscar/$', buscar.as_view(), name="buscar"),
]

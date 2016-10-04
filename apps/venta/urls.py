from django.conf.urls import url
from apps.venta.views import index,registro_venta

urlpatterns=[
    url(r'^$',index,name='index'),
    url(r'^registrar_venta/$',registro_venta,name="registro"),
]

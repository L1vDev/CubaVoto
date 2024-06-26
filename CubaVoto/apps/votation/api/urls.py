from django.conf.urls import include
from django.urls import path
from apps.votation.api.views import Diputados_View, Provincia_View, Municipio_View, Usuarios_View
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('diputados', Diputados_View, basename='diputados')
router.register('provincia', Provincia_View, basename='provincia')
router.register('municipio', Municipio_View, basename='municipio')
router.register('usuarios', Usuarios_View, basename='usuarios')


urlpatterns=[
    path("",include(router.urls)),
]
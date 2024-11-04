from django.conf.urls import include
from django.urls import path
from apps.votation.api.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

router=DefaultRouter()
router.register('diputados', Diputados_View, basename='diputados')
#router.register('diputados/<int:ci>/', Votacion_View, basename='votacion')
router.register('provincia', Provincia_View, basename='provincia')
router.register('municipio', Municipio_View, basename='municipio')
router.register('usuarios', Usuarios_View, basename='usuarios')


urlpatterns=[
    path("",include(router.urls)),
    path("votacion/<str:user>/",Votacion_View.as_view(),name="votar"),
    #path("votacion/<str:user>/<str:dip>/",Votacion_View.as_view(),name="votacion"),
    path('token/', UserToken_View.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("login/", Login_View.as_view(), name="login")

]
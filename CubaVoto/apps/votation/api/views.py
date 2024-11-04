from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.votation.models import Diputados, Municipio, Provincia, Persona
from apps.votation.api.serializers import *
from django.contrib.auth import authenticate

class UserToken_View(TokenObtainPairView):
    serializer_class=UserToken_Serializer

class Diputados_View(viewsets.ModelViewSet):
    queryset=Diputados.objects.all()
    serializer_class = Diputados_Serializer

class Municipio_View(viewsets.ModelViewSet):
    queryset=Municipio.objects.all()
    serializer_class = Municipio_Serializer

class Provincia_View(viewsets.ModelViewSet):
    queryset=Provincia.objects.all()
    serializer_class = Provincia_Serializer

class Usuarios_View(viewsets.ModelViewSet):
    queryset=Persona.objects.all()
    serializer_class=Usuario_Serializer

class Votacion_View(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, user):
        try:
            filtro=Persona.objects.get(ci=user)
            object_query=Diputados.objects.filter(provincia=filtro.provincia)
            serializer=Diputados_Serializer(object_query, many=True)
            return Response(serializer.data)
        except Persona.DoesNotExist:
            return Response({"Error":"No existe el usuario"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user):
        usuario=Persona.objects.get(ci=user)
        diputado=Diputados.objects.get(pk=request.data['id'])
        if not usuario.voto:
            if 'votos' not in request.data.keys():
                request.data['votos']=diputado.votos+1
            else:
                request.data['votos']=request.data['votos']+1
            us_data={
                "ci":usuario.ci,
                "nombre":usuario.nombre,
                "edad":usuario.edad,
                "voto":True,
                "provincia":usuario.provincia.pk,
                "municipio":usuario.municipio.pk
            }
            us_deserializer=Usuario_Serializer(usuario, data=us_data)
            if us_deserializer.is_valid():
                us_deserializer.save()
            else:
                return Response(us_deserializer.errors)
        else:
            return Response({"error": "El usuario ha realizado su voto"})
     
        dip_deserializer=Diputados_Serializer(diputado, data=request.data)
        if dip_deserializer.is_valid():
            print("Voto exitoso")
            dip_deserializer.save()
            return Response(dip_deserializer.data)
        else:
            return Response(dip_deserializer.errors)
        
class Login_View(APIView):
    def post(self, request):
        serializer = Login_Serializer(data=request.data)
        if serializer.is_valid():
            ci = serializer.validated_data['ci']
            nombre = serializer.validated_data['nombre']
            user = authenticate(request,ci=ci, nombre=nombre)
            print(ci)
            print(nombre)
            print(user)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
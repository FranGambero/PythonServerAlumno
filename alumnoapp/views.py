from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Alumnos
from .serializers import AlumnosSerializers
from rest_framework.response import Response
from rest_framework import status


class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializers

    def delete(self, request, pk, format=None):
        alumno= self.get_object(pk)
        alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
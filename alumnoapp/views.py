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

    def put(self, request, pk, format=None):
        alumno= self.get_object(pk)
        serializer = AlumnosSerializers(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
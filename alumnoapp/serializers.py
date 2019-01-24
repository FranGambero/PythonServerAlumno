from rest_framework import serializers
from .models import Alumnos

class AlumnosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = '__all__'   # si ponemos esto hace le CRUD de operaciones
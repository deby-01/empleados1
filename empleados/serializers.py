from rest_framework import serializers
from .models import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model= Perfil
        fields=('id','foto','nombre_user','nombres','apellidos','rut','edad','fecha_nac',
                'genero','correo','comuna','direccion','telefono','fecha_creacion',
                'area','cargo','sueldo_base')
        read_only_fields= ('id',)
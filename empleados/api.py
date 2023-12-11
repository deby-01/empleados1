from empleados.models import Perfil
from rest_framework import viewsets, permissions
from .serializers import PerfilSerializer

class PerffilViewSet(viewsets.ModelViewSet):
    queryset= Perfil.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= PerfilSerializer

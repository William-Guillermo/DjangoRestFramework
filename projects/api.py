from .models import Project
from rest_framework import viewsets, permissions
from .serializer import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    #consultas que se podran hacer 
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]   # que personas tiene permisos para las consultas, cualquier cliente puede consutar datos al server
    serializer_class = ProjectSerializer


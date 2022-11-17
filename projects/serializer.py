from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    La clase Meta se puede usar para definir varias cosas sobre el modelo, como los permisos, 
    el nombre de la base de datos, los nombres singulares y plurales.
    """
    class Meta:
        model=Project
        #campos a ser consultados
        fields = ('id','title','description','technology','created_at')
        # read_only_fields  variable que declara que campos seran de solo lectura y no se ocupan que sean modificados
        read_only_fields = ('crated_at',)  #colocar una coma al final si no envia error ya que espera una tupla
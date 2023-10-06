from rest_framework import serializers
from evaseg_app.models import Rol, TipoDocumento, Usuario, Login, Ficha, AprendizFicha, InstructorFicha, TipoProceso, Proceso, Citacion, DetalleProceso

# ---serializador de tabla Rol---
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

# ---serializador de tabla TipoDocumento---
class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

# ---serializador de tabla Usuario---
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# ---serializador de tabla Login---
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

# ---serializador de tabla Ficha---
class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = '__all__'

# ---serializador de tabla AprendizFicha---
class AprendizFichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AprendizFicha
        fields = '__all__'

# ---serializador de tabla InstructorFicha---
class InstructorFichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorFicha
        fields = '__all__'

# ---serializador de tabla TipoProceso---
class TipoProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProceso
        fields = '__all__'

# ---serializador de tabla Proceso---
class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = '__all__'

# ---serializador de tabla Citacion---
class CitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citacion
        fields = '__all__'

# ---serializador de tabla DetalleProceso---
class DetalleProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleProceso
        fields = '__all__'


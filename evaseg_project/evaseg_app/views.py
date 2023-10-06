from rest_framework.response import Response
from rest_framework.views import APIView
from evaseg_app.models import  Rol, TipoDocumento, Usuario, Login, Ficha, AprendizFicha, InstructorFicha, TipoProceso, Proceso, Citacion, DetalleProceso
from evaseg_app.serializers import RolSerializer, TipoDocumentoSerializer,  UsuarioSerializer, LoginSerializer, FichaSerializer, AprendizFichaSerializer, InstructorFichaSerializer, TipoProcesoSerializer, ProcesoSerializer, CitacionSerializer, DetalleProcesoSerializer

class RolList(APIView):
    def get(self, request):
        rol = Rol.objects.all()
        rol_serializer = RolSerializer(rol, many = True)
        return Response(rol_serializer.data)
    
class TipoDocumentoList(APIView):
    def get(self, request):
        tipodocumento = TipoDocumento.objects.all()
        tipodocumento_serializer = TipoDocumentoSerializer(tipodocumento, many = True)
        return Response(tipodocumento_serializer.data)

class UsuarioList(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuarios, many=True)
        return Response(usuario_serializer.data)

class LoginList(APIView):
    def get(self, request):
        logins = Login.objects.all()
        logins_serializer = LoginSerializer(logins, many=True)
        return Response(logins_serializer.data)

class FichaList(APIView):
    def get(self, request):
        fichas = Ficha.objects.all()
        fichas_serializer = FichaSerializer(fichas, many=True)
        return Response(fichas_serializer.data)

class AprendizFichaList(APIView):
    def get(self, request):
        aprendicesFichas = AprendizFicha.objects.all()
        aprendicesFichas_serializer = AprendizFichaSerializer(aprendicesFichas, many=True)
        return Response(aprendicesFichas_serializer.data)

class InstructorFichaList(APIView):
    def get(self, request):
        instructoresFichas = InstructorFicha.objects.all()
        instructoresFichas_serializer = InstructorFichaSerializer(instructoresFichas, many=True)
        return Response(instructoresFichas_serializer.data)

class TipoProcesoList(APIView):
    def get(self, request):
        tipoProceso = TipoProceso.objects.all()
        tipoProceso_serializer = TipoProcesoSerializer(tipoProceso, many=True)
        return Response(tipoProceso_serializer.data)

class ProcesoList(APIView):
    def get(self, request):
        procesos = Proceso.objects.all()
        procesos_serializer = ProcesoSerializer(procesos, many=True)
        return Response(procesos_serializer.data)

class CitacionList(APIView):
    def get(self, request):
        citaciones = Citacion.objects.all()
        citaciones_serializer = CitacionSerializer(citaciones, many=True)
        return Response(citaciones_serializer.data)

class DetalleProcesoList(APIView):
    def get(self, request):
        detallesProceso = DetalleProceso.objects.all()
        detallesProceso_serializer = DetalleProcesoSerializer(detallesProceso, many=True)
        return Response(detallesProceso_serializer.data)

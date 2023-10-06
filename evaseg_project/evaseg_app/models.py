from django.db import models

# Modelo para la tabla "roles"
class Rol(models.Model):
    tipoRol = models.CharField(max_length = 50, null=True)
    descripcionRol = models.CharField(max_length = 100, null=True)


# Modelo para la tabla "tipoDocumento"
class TipoDocumento(models.Model):
    tipoDocumento = models.CharField(max_length=50)
    siglasTipoDocumento = models.CharField(max_length=3)

# Modelo para la tabla "usuarios"
class Usuario(models.Model):
    numeroDocumento = models.CharField(max_length=12, primary_key=True)
    tipoDocumentoFK = models.ForeignKey(TipoDocumento, null=True, on_delete=models.SET_NULL)
    idRolFK = models.ForeignKey(Rol, null=True, on_delete=models.SET_NULL)
    primerNombreUsuario = models.CharField(max_length=30)
    segundoNombreUsuario = models.CharField(max_length=30, blank=True, null=True)
    primerApellidoUsuario = models.CharField(max_length=40)
    segundoApellidoUsuario = models.CharField(max_length=40, blank=True, null=True)
    correoUsuario = models.CharField(max_length=60)
    telefonoUsuario = models.CharField(max_length=10)
    direccionUsuario = models.CharField(max_length=40)

# Modelo para la tabla "login"
class Login(models.Model):
    numeroDocumentoFK = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=40)

# Modelo para la tabla "fichas"
class Ficha(models.Model):
    idFicha = models.CharField(max_length=7, primary_key=True)
    centroSena = models.CharField(max_length=60)
    dependenciaSena = models.CharField(max_length=50)
    programaFormacion = models.CharField(max_length=60)

# Modelo para la tabla "instructorFicha"
class InstructorFicha(models.Model):
    idFichaFK = models.ForeignKey(Ficha, null=True, on_delete=models.SET_NULL)
    idInstructorFK = models.OneToOneField(Usuario, null=True, on_delete=models.SET_NULL)

# Modelo para la tabla "aprendizFicha"
class AprendizFicha(models.Model):
    idFichaFK = models.ForeignKey(Ficha, null=True, on_delete=models.SET_NULL)
    idAprendizFK = models.OneToOneField(Usuario, null=True, on_delete=models.SET_NULL)

# Modelo para la tabla "tipoProceso"
class TipoProceso(models.Model):
    nombreTipoProceso = models.CharField(max_length=30)
    descripcionTipoProceso = models.TextField()

# Modelo para la tabla "proceso"
class Proceso(models.Model):
    tipoProcesoFK = models.ForeignKey(TipoProceso, on_delete=models.CASCADE)
    idInstructorFK = models.OneToOneField(InstructorFicha, on_delete=models.CASCADE)
    idAprendizFK = models.OneToOneField(AprendizFicha, on_delete=models.CASCADE)
    fechaCreacionProceso = models.DateField()
    causasProceso = models.TextField()
    RutaEvidenciasProceso = models.TextField()

# Modelo para la tabla "citacion"
class Citacion(models.Model):
    idProcesoFK = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    fechaHoraCitacion = models.DateTimeField()

# Modelo para la tabla "detalleProceso"
class DetalleProceso(models.Model):
    idProcesoFK = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    fechaHorainicioProceso = models.DateTimeField()
    fechaHoraFinProceso = models.DateTimeField()
    calificacionGravedadProceso = models.CharField(max_length=30)
    decargosProceso = models.TextField()
    rutaEvidenciasDescargosProceso = models.TextField()
    detallesProceso = models.TextField()
    decisionProceso = models.TextField()


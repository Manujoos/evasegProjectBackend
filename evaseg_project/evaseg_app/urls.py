from django.urls import path
from . import views

urlpatterns = [
    path('rol/', views.RolList.as_view(), name = 'rol_api'),   
    path('tipodocumento/', views.TipoDocumentoList.as_view(), name = 'tipodocumento_api'),
    path('usuario', views.UsuarioList.as_view(), name = 'usuario_api'),
    path('login/', views.LoginList.as_view(), name='login_api'),
    path('ficha/', views.FichaList.as_view(), name='ficha_api'),
    path('aprendizficha/', views.AprendizFichaList.as_view(), name='aprendizficha_api'),
    path('instructorficha/', views.InstructorFichaList.as_view(), name='instructorficha_api'),
    path('tipoproceso/', views.TipoProcesoList.as_view(), name='tipoproceso_api'),
    path('proceso/', views.ProcesoList.as_view(), name='proceso_api'),
    path('citacion/', views.CitacionList.as_view(), name='citacion_api'),
    path('detalleproceso/', views.DetalleProcesoList.as_view(), name='detalleproceso_api')
]



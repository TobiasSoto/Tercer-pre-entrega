from django.urls import path
from .views import  *



urlpatterns = [
    path('', inicio, name="inicio"),
    path('agrega-grupo/<nombre>/<camada>', curso),
    path('lista-cursos/', listar_cursos),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('cursoFormulario/', cursoFormulario, name="cursoFormulario"),
    path('FormularioEstudiante/', FormularioEstudiantes, name="FormularioEstudiantes"),
    path('BusquedaCamada/', BusquedaCamada , name="BusquedaCamada"),
    path('buscar/',buscar , name="Buscar"),
    path('FormularioLibros/', FormularioLibros, name="FormularioLibros"),

    

    ]
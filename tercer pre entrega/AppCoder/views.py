
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Curso, Estudiante, Libro
from datetime import datetime
from django.template import Template, Context, loader
from .forms import FormularioCurso, FormularioEstudiante, FormularioLibros1


def curso(req, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
    <p> Curso: {curso.nombre} - Camada: {curso.camada} creado con exito! </p>
    """)

def listar_cursos(req):

    lista = Curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos":lista})

def inicio(req):

    return render(req, "inicio.html")

def cursos(req):

    return render(req, "cursos.html")

def profesores(req):

    return render(req, "profesores.html")

def entregables(req):

    return render(req, "entregables.html")

def estudiantes(req):

    return render(req, "estudiantes.html")


def cursoFormulario(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        
        miFormulario = FormularioCurso(req.POST)
        
        if miFormulario.is_valid():

            data=miFormulario.cleaned_data

            curso=Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()
        

            return render(req, "inicio.html")
    
    else: 
        miFormulario = FormularioCurso()
        return render(req, "cursoFormulario.html",{"miFormulario":miFormulario})
    


def FormularioEstudiantes(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
    
        miFormulario1 = FormularioEstudiante(req.POST)

        if miFormulario1.is_valid():
            data=miFormulario1.cleaned_data
            estudiante=Estudiante(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            estudiante.save()

            return render(req, "inicio.html")
    else:
        miFormulario1 =FormularioEstudiante()
        return render(req, "formularioestudiantes.html",{"miFormulario1":miFormulario1})


def BusquedaCamada(req):
    return render(req, "busquedacamada.html")

def buscar(req: HttpRequest):
    if "camada" in req.GET:
        try:
            camada = req.GET["camada"]
        except ValueError:
            return HttpResponse("Ingrese una camada válida")

        try:
            curso = Curso.objects.get(camada=camada)
            return render(req, "resultadobuscar.html", {"curso": curso})
        except Curso.DoesNotExist:
            return HttpResponse(f"No se encontró un curso con la camada '{camada}'")
    else:
        return HttpResponse("Debe agregar una camada en la consulta")
    

def FormularioLibros(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
    
        miFormulario2 = FormularioLibros1(req.POST)

        if miFormulario2.is_valid():
            data=miFormulario2.cleaned_data
            libro=Libro(nombre=data["nombre"], precio=data["precio"], numerodeguardado=data["numerodeguardado"])
            libro.save()

            return render(req, "inicio.html")
    else:
        miFormulario2 =FormularioLibros1()
        return render(req, "formulariolibros.html",{"miFormulario2":miFormulario2})
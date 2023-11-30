from django import forms
class FormularioCurso(forms.Form):

    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class FormularioEstudiante(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class FormularioLibros1(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    numerodeguardado = forms.IntegerField()
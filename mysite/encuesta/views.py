from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Desde la visa de encuestas!")

def detalle(request, pregunta_id):
    return HttpResponse("Estas viendo la pregunta %s." %pregunta_id)

def resultados(request, pregunta_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response %pregunta_id)

def votar(request, pregunta_id):
    return HttpResponse("Estas votando por la pregunta %s." %pregunta_id)

def suma(request, dato1, dato2):
    resultado=dato1+dato2
    return HttpResponse("Resultado: \n La suma de %s + %s es igual a %s" %(dato1,dato2,resultado))

def resta(request, dato1, dato2):
    resultado=dato1-dato2
    return HttpResponse("Resultado: \n La resta de %s - %s es igual a %s" %(dato1,dato2,resultado))

def multiplicacion(request, dato1, dato2):
    resultado=dato1*dato2
    return HttpResponse("Resultado: \n La multiplicación de %s * %s es igual a %s" %(dato1,dato2,resultado))

def division(request, dato1, dato2):
    resultado=dato1/dato2
    return HttpResponse("Resultado: \n La división de %s / %s es igual a %s" %(dato1,dato2,resultado))

def pagoSemanal(request,horas,pph):
    if (horas<=40):
        total = horas*pph
    else:
        total = 2*pph*(horas-40)+pph*40
    return HttpResponse("El pago semanal es de %s soles." %total)

def geometria(request,b,h):
    area=b*h
    perimetro=2*(b+h)
    return HttpResponse("El Área es %s y el Perímetro es %s." %(area,perimetro))
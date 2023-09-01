from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: localhost:8080/polls/5/
    path('<int:pregunta_id>/', views.detalle, name='detail'),
    # ex: localhost:8080/polls/5/results/
    path('<int:pregunta_id>/results/', views.resultados, name='results'),
    # ex: localhost:8080/polls/5/vote/
    path('<int:pregunta_id>/vote/', views.votar, name='vote'),

## EJERCICIO 21
    # localhost:8080/polls/sumar/18/19
    path('sumar/<int:dato1>/<int:dato2>', views.suma, name='suma'),
    # localhost:8080/polls/restar/18/19
    path('restar/<int:dato1>/<int:dato2>', views.resta, name='resta'),
    # localhost:8080/polls/multiplicar/18/19
    path('multiplicar/<int:dato1>/<int:dato2>', views.multiplicacion, name='multiplicacion'),
    # localhost:8080/polls/dividir/18/19
    path('dividir/<int:dato1>/<int:dato2>', views.division, name='division'),

##EJERCICIO 22

    # localhost:8080/polls/pagoSemanal/41/20
    path('pagoSemanal/<int:horas>/<int:pph>',views.pagoSemanal,name='pagoSemanal'),

##EJERCICIO 23

    # localhost:8080/polls/geometria/2/3
    path('geometria/<int:b>/<int:h>',views.geometria,name='geometria'),



]

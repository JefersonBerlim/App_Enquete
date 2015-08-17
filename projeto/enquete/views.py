#-*- coding:utf8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from enquete.models import Enquete
#from forms import FormEnquete
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Enquete(request):	
	return render_to_response('RespondeEnquete.html')


@csrf_exempt
def RespondeEnquete(request):

    formulario = Enquete(request.POST)

   	formulario.save()

    return render_to_response( 'index.html', {'minhavariavel':formulario} )


def Mensagem():
	return render_to_response( 'Mensagem.html', {'email': email} )
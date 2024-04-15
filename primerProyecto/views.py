from django.http import HttpResponse
def saludo(request):
    return HttpResponse("saludo")

def holaMundo(request):
    return HttpResponse("Hola mundo ")
def mayoriaEdad(request,edad):
    if edad < 18:
        return HttpResponse("Eres menor de edad")
    else:
        return HttpResponse("Eres mayor de edad")

from django.http import HttpResponse
def  index(request):
    return  HttpResponse("<h1>This is the current homepage!!!!<h1>")
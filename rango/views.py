from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello U r At Polls Index")
    
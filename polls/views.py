from django.http import HttpResponse


def index(request):
    response_text = "Hello, world. You're at the polls index."
    return HttpResponse(response_text)

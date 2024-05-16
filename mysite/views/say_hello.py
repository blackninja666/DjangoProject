from django.http import HttpResponse


def my_view(request):
    return HttpResponse("<html>Hello, Welcome to MySite</html>")


def my_view2(request, name):
    print(request.headers)
    print(request.GET)
    print(request.content_params)
    return HttpResponse("Hello, %s! Welcome to MySite Again! :)" % name)
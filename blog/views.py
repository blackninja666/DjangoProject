from django.http import HttpResponse


def blog_view(request):
    return HttpResponse("This is your first blog view!")
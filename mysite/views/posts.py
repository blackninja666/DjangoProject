from django.http import HttpResponse


def view_posts(request, post_id):
    return HttpResponse("Hey, here is your post #%s!" % post_id)
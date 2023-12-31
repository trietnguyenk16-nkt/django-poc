from django.http import HttpResponse
from django.template import loader


def portal(request):
    template = loader.get_template('portal.html')
    return HttpResponse(template.render())


def thankyou(request):
    template = loader.get_template('thankyou.html')
    return HttpResponse(template.render())

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from ielts.models import Seat


def show(request):
    seats = Seat.objects.all()
    t = loader.get_template("index.html")
    c = Context({'seats': seats})
    return HttpResponse(t.render(c))


def subscribe(request):
    t = loader.get_template("subscribe.html")
    c = Context()
    return HttpResponse(t.render(c))


def search(request):
    if 'place' in request.GET:
        key = request.GET['place']
        # print 'key: ' + key
        seats = Seat.objects.filter(city__icontains=key)
        if not seats: # if city can not found, try to search province
            seats = Seat.objects.filter(province__icontains=key)

        t = loader.get_template("index.html")
        c = Context({'seats': seats})
        return HttpResponse(t.render(c))
    else:
        msg = 'You submitted an empty form.'
        return HttpResponse(msg)
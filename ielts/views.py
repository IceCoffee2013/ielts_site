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
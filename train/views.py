from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from train.models import Account


def show(request):
    seats = []
    t = loader.get_template("index_12306.html")
    c = Context({'seats': seats})
    return HttpResponse(t.render(c))

def search(request):
    if 'place' in request.GET:
        key = request.GET['place']
        # print 'key: ' + key
        seats = Account.objects.filter(name__contains=key)
        # if not seats: # if city can not found, try to search province
        #     seats = Seat.objects.filter(province__icontains=key)

        t = loader.get_template("index_12306.html")
        c = Context({'seats': seats})
        return HttpResponse(t.render(c))
    else:
        msg = 'You submitted an empty form.'
        return HttpResponse(msg)
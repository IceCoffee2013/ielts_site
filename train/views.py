from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from train.models import Account


def show(request):
    seats = []
    t = loader.get_template("query_12306.html")
    c = Context({'seats': seats})
    return HttpResponse(t.render(c))

def search(request):
    if 'place' in request.GET:
        key = request.GET['place']
        # print 'key: ' + key
        seats = Account.objects.filter(name__contains=key)
        # if not seats: # if city can not found, try to search province
        #     seats = Seat.objects.filter(province__icontains=key)

        try:
            for i in seats:
                private_phone = i.phone
                i.phone = private_phone[:3] + '****' + private_phone[-4:]
                private_cardId = i.cardId
                i.cardId = private_cardId[:8] + '******' + private_cardId[-4:]
        except Exception,e:
            print e

        t = loader.get_template("index_12306.html")
        c = Context({'seats': seats})
        return HttpResponse(t.render(c))
    else:
        msg = 'You submitted an empty form.'
        return HttpResponse(msg)
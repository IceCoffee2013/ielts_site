import logging
from django.http import HttpResponse

# Create your views here.
from django.template import loader, Context
from photo_grasp import parsers


def show(request):
    seats = []
    t = loader.get_template("query_photo.html")
    c = Context({'seats': seats})
    return HttpResponse(t.render(c))

def search(request):
    if 'place' in request.GET:
        key = request.GET['place']
        print 'key: ' + key
        logging.debug('key: ' + key)  #
        # seats = Account.objects.filter(name__contains=key)
        # # if not seats: # if city can not found, try to search province
        # #     seats = Seat.objects.filter(province__icontains=key)
        #
        # try:
        #     for i in seats:
        #         private_phone = i.phone
        #         i.phone = private_phone[:3] + '****' + private_phone[-4:]
        #         private_cardId = i.cardId
        #         i.cardId = private_cardId[:8] + '******' + private_cardId[-4:]
        # except Exception,e:
        #     print e

        uri_list = parsers.parse_tuchong_photo(key)

        t = loader.get_template("index_photo.html")
        c = Context({'uris': uri_list})
        return HttpResponse(t.render(c))
    else:
        msg = 'You submitted an empty form.'
        return HttpResponse(msg)
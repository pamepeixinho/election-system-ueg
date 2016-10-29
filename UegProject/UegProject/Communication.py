import simplejson as simplejson
from django.http import HttpResponse
from django.http import JsonResponse
from numpy.distutils.fcompiler import none


def teste(request):
    return HttpResponse('Teste')


def teste1(request):
    return JsonResponse({'Json': 'teste'})


def teste2(request):
    some_data_to_dump = {
        'some_var_1': 'foo',
        'some_var_2': 'bar',
    }

    data = simplejson.dumps(some_data_to_dump)
    return HttpResponse(data, content_type="application/json")


def teste3(request, uev_id):
    uevJson = {
        'uev_id': uev_id,
    }

    data = simplejson.dumps(uevJson)
    return HttpResponse(data, content_type="application/json")


def teste4(request):
    query = request.GET.get('query')
    uev_id = request.GET.get('uev_id')

    uevJson = {
        'uev_id': uev_id,
        'query': query,
    }

    data = simplejson.dumps(uevJson)
    return HttpResponse(data, content_type="application/json")


class Communication(object):
    ueg = none

    def sendData(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')

        uevJson = {
            # TODO get array
            'voter': 'eleitor',
            'candidate': 'candidate',
        }

        data = simplejson.dumps(uevJson)
        return HttpResponse(data, content_type="application/json")

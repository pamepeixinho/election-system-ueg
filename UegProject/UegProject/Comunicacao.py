import simplejson as simplejson
from django.http import HttpResponse
from django.http import JsonResponse


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
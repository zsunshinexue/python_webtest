import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def test1(request):
    return HttpResponse('首页')


def test2(request):
    response = HttpResponse(json.dumps({"name": "tom", "age": "12"  , "code":20000}))

    # response['Access-Control-Allow-Origin'] = '*'
    #
    # response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    #
    # response['Access-Control-Max-Age'] = '1000'
    #
    # response['Access-Control-Allow-Headers'] ='*'

    return response

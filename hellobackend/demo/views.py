from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def hello(request):

    if request.method== 'GET':
        return JsonResponse({"name":"aaaa"}, safe=False)



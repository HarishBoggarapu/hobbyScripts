from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View
from .mixins import JsonHttpMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

sampleData = {
    "name": "Harish",
    "city": "Tempe",
    "state": "AZ",
    "team": "Philadelphia Eagles"
}

# Create your views here.


@csrf_exempt
def sampleHTML(requests):
    return HttpResponse('<h1>Hello, this is HTML response</h1>')


def sampleJSON(request):
    return HttpResponse(json.dumps(sampleData), content_type='application/json')

# All class based views are child of View
# They provide functionality for various REST methods (PUT,GET,POST,DELETE)


class jsonCBV(View, JsonHttpMixin):
    def get(self, request, *args, **kwargs):
        return self.renderJsonResponse(sampleData)


@method_decorator(csrf_exempt, name='dispatch')
class jsonCBVPost(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>Sample GET response</h1>')

    def post(self, request, *args, **kwargs):
        return HttpResponse('<h1>Sample POST response</h1>')

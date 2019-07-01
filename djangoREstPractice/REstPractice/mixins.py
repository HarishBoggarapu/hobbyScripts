from django.http import HttpResponse
import json


class JsonHttpMixin:
    def renderJsonResponse(self, jsonData):
        return HttpResponse(json.dumps(jsonData), content_type='application/json')

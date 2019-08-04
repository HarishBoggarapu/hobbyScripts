from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('sampleJSON/', views.sampleJSON, name='sample-json'),
    path('sampleHTML/', views.sampleHTML, name="sample-html"),
    path('jsonCBV/', views.jsonCBV.as_view(), name="jsonCBV"),
    url(r'^jsonCBVPOST/$', views.jsonCBVPost.as_view(), name="jsonCBVPOST")
]

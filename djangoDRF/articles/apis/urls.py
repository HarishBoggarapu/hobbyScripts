from django.urls import path, include
from django.conf.urls import url
from articles.apis import views

urlpatterns = [
    path('get/', views.articleOp.as_view(), name='article-get'),
    path('delete/<int:id>', views.articleOp.as_view(), name='article-delete'),
    path('getG/', views.articleGOp.as_view(), name='article-delete')
]

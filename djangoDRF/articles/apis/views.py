from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import Article
from articles.apis.serializers import ArticleSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView


@permission_classes((permissions.AllowAny,))
class articleOp(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'articles': serializer.data})

    def delete(self, request, id):
        article = get_object_or_404(Article.objects.all(), pk=id)
        article.delete()
        return Response({'success': 'article with id {} was deleted'.format(id)})


@permission_classes((permissions.AllowAny,))
class articleGOp(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

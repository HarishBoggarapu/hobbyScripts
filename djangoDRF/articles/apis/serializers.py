from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
    # title = serializers.CharField(max_length=120)
    # content = serializers.CharField()
    # author_id = serializers.IntegerField()

    # def create(self, validate_data):
    #     return Article.objects.create(**validate_data)

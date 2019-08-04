from django.contrib import admin

from articles.models import Article, Author

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    display_list = ['title', 'content']


class AuthorAdmin(admin.ModelAdmin):
    display_list = ['name', 'email']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)

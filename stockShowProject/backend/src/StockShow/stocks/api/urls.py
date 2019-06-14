from django.urls import path
from .views import StockListView, StockDetailView

urlpatterns = [
    path('', StockListView.as_view()),
    path('<pk>', StockDetailView.as_view())

    # path('about/', views.about, name='stocks-about'),
]

from rest_framework.generics import ListAPIView, RetrieveAPIView
from stocks.models import Stock
from stocks.api.serializers import StockSerializer


class StockListView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDetailView(RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

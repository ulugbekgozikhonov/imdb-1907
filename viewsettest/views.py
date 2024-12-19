from rest_framework import viewsets

from watchlist_app.models import WatchList
from watchlist_app.serializers import WatchListSerializer


class WatchListViewSet(viewsets.ModelViewSet):
	queryset = WatchList.objects.all()
	serializer_class = WatchListSerializer

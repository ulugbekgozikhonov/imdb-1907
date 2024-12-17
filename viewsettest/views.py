from rest_framework import viewsets

from api.models import WatchList
from api.serializers import WatchListSerializer


class WatchListViewSet(viewsets.ModelViewSet):
	queryset = WatchList.objects.all()
	serializer_class = WatchListSerializer

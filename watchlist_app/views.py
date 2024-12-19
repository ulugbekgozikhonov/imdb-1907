from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.permissions import IsAdminOrReadOnly
from watchlist_app.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer


class WatchListAPIView(APIView):
	permission_classes = [IsAdminOrReadOnly]

	def get(self, request):
		watchlist = WatchList.objects.all()
		serializer = WatchListSerializer(watchlist, many=True, context={'request': request})
		return Response(serializer.data)

	def post(self, request):
		serializer = WatchListSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)


class WatchDetailAPIView(APIView):
	def get(self, request, pk):
		watchlist = WatchList.objects.get(pk=pk)
		serializer = WatchListSerializer(instance=watchlist)
		return Response(serializer.data)

	def put(self, request, pk):
		watchlist = WatchList.objects.get(pk=pk)
		serializer = WatchListSerializer(instance=watchlist, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=400)

	def delete(self, request, pk):
		watchlist = WatchList.objects.get(pk=pk)
		watchlist.delete()
		return Response(status=204)


class StreamPlatformAPIView(APIView):
	def get(self, request):
		stream_platforms = StreamPlatform.objects.all()
		serializer = StreamPlatformSerializer(stream_platforms, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = StreamPlatformSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)


class StreamPlatformDetailAPIView(APIView):

	def get(self, request, pk):
		stream = StreamPlatform.objects.get(pk=pk)
		serializer = StreamPlatformSerializer(instance=stream)
		return Response(serializer.data)


class ReviewAV(generics.ListCreateAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = ReviewSerializer
	queryset = Review.objects.all()

	def perform_create(self, serializer):
		pk = self.kwargs['pk']

		watchlist = get_object_or_404(WatchList, pk=pk)

		review = Review.objects.filter(watchlist=watchlist, user=self.request.user)
		if review.exists():
			raise ValidationError("You have already reviewed this movie")

		watchlist.rating_number += 1
		watchlist.rating_sum += serializer.validated_data['rating']
		watchlist.rating = watchlist.rating_sum / watchlist.rating_number
		watchlist.save()
		serializer.save(watchlist=watchlist, user=self.request.user)

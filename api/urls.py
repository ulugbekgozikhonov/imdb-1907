from django.urls import path

from .views import WatchListAPIView, StreamPlatformAPIView, StreamPlatformDetailAPIView, ReviewAV

urlpatterns = [
	path('watchlist/', WatchListAPIView.as_view(), name="watchlist"),
	path('watchlist/<int:pk>/review/', ReviewAV.as_view(), name="review"),
	path('watchlist/<int:pk>', StreamPlatformDetailAPIView.as_view(), name="stream-detail"),
	path('stream/', StreamPlatformAPIView.as_view()),
]

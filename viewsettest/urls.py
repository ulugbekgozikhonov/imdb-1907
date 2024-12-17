from django.urls import path, include
from rest_framework.routers import DefaultRouter

from viewsettest import views

router = DefaultRouter()
router.register('wr', views.WatchListViewSet)
urlpatterns = [
	path('', include(router.urls)),
]

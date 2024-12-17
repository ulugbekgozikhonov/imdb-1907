from django.contrib import admin

from api.models import WatchList, StreamPlatform


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
	list_display = ["id", "name"]

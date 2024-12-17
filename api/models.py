from django.db import models


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class StreamPlatform(BaseModel):
	name = models.CharField(max_length=100)
	about = models.TextField()
	website = models.URLField()

	class Meta:
		verbose_name = "StreamPlatform"
		verbose_name_plural = "StreamPlatforms"

	def __str__(self):
		return self.name


class WatchList(BaseModel):
	title = models.CharField(max_length=100)
	rating_sum = models.PositiveIntegerField()
	description = models.TextField()
	rating = models.FloatField()
	rating_number = models.PositiveIntegerField()
	is_active = models.BooleanField(default=True)
	stream = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name = "WatchList"
		verbose_name_plural = "WatchLists"

	def __str__(self):
		return self.title


class Review(BaseModel):
	rating = models.PositiveIntegerField()
	description = models.TextField()
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviews')
	watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')

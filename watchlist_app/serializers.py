from rest_framework import serializers

from watchlist_app.models import StreamPlatform, WatchList, Review


class StreamPlatformSerializer(serializers.ModelSerializer):
	# watchlist = WatchListSerializer(many=True, read_only=True)

	class Meta:
		model = StreamPlatform
		fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
	stream = StreamPlatformSerializer(read_only=True)
	rating = serializers.FloatField(read_only=True)
	rating_number = serializers.IntegerField(read_only=True)
	is_active = serializers.BooleanField(read_only=True)

	class Meta:
		model = WatchList
		fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
	user = serializers.StringRelatedField(read_only=True)
	watchlist = serializers.StringRelatedField(read_only=True)

	class Meta:
		model = Review
		fields = '__all__'

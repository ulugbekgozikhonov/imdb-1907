from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ["username", "email", "password", "password2"]

	def save(self, **kwargs):
		password = self.validated_data.get("password")
		password2 = self.validated_data.get("password2")

		if password != password2:
			raise serializers.ValidationError("Passwords must match.")
		if User.objects.filter(username=self.validated_data["username"]).exists():
			raise serializers.ValidationError("Username already exists.")
		user = User(username=self.validated_data["username"], email=self.validated_data["email"])
		user.set_password(password)
		user.save()
		return user

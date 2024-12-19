from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_app.api.serializers import UserSerializer


@api_view(['POST'])
def register(request):
	serializer = UserSerializer(data=request.data)
	data = {}
	if serializer.is_valid():
		user = serializer.save()
		data['username'] = user.username
		data['email'] = user.email
		data['token'] = Token.objects.get(user=user).key
		return Response(data, status=201)

	return Response(serializer.errors, status=400)

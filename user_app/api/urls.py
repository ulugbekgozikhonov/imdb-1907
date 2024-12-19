from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user_app.api.views import register

urlpatterns = [
	path('login/', obtain_auth_token),
	path('register/', register),
]

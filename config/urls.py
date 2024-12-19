from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include("watchlist_app.urls")),
	path('account/', include('user_app.api.urls')),
	path('watchlist_app-auth/', include("rest_framework.urls")),
	path('', include("viewsettest.urls")),
]

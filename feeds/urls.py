from django.contrib import admin
from django.urls import path, include  # Include is needed for the app's URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feeds/', include('feeds.urls')),  # Include the feeds app's URLs
]

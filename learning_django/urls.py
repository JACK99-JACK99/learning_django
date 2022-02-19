
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('', include('App1.urls')),
    path('', include('quickstart.urls')),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls'))
]

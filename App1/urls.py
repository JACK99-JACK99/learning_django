from django.urls import path, include
from .views import Testview

urlpatterns = [
    path('', Testview.as_view(), name='test'),
    path('api-auth/', include('rest_framework.urls'))
]
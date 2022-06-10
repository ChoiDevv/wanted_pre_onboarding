from django.urls import include, path
from rest_framework import routers

from api.views import UserViewSet

api_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
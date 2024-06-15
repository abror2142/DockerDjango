from django.urls import path, include
from rest_framework import routers

from .views import UserProfileAPIView

router = routers.SimpleRouter()
router.register('user', UserProfileAPIView)


urlpatterns = [
    path('', include(router.urls)),
]

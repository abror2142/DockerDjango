from django.urls import path, include
from rest_framework import routers

from .views import MessageAPIView, FollowerAPIView


router = routers.SimpleRouter()
router.register('message', MessageAPIView)
router.register('follower', FollowerAPIView)


urlpatterns = [
    path('v1/', include(router.urls)),
]

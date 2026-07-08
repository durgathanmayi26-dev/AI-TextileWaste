from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TextileWasteViewSet

router = DefaultRouter()
router.register(r'textiles', TextileWasteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

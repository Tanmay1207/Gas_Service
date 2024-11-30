from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet, CustomerAccountViewSet

router = DefaultRouter()
router.register(r'service-requests', ServiceRequestViewSet)
router.register(r'customer-accounts', CustomerAccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


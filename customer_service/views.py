from rest_framework import viewsets, permissions
from .models import ServiceRequest, CustomerAccount
from .serializers import ServiceRequestSerializer, CustomerAccountSerializer

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ServiceRequest.objects.all()
        return ServiceRequest.objects.filter(customer=user)

class CustomerAccountViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerAccount.objects.all()
    serializer_class = CustomerAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return CustomerAccount.objects.all()
        return CustomerAccount.objects.filter(user=user)


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Storage
from .serializers import StorageSerializer
from .permissions import IsCompanyMember


class StorageViewSet(viewsets.ModelViewSet):
    serializer_class = StorageSerializer
    permission_classes = [IsAuthenticated, IsCompanyMember]

    def get_queryset(self):
        if hasattr(self.request.user, 'company'):
            return Storage.objects.filter(company=self.request.user.company)
        return Storage.objects.none()

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)
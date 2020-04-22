from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead ViewSet
# Create UPDATE etc FUNCTIONS without need to specify


class LeadViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.request.user.leads.all()
    # We need to specify a serial class which is LS

    # Save the lead owner when we create the lead
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

from rest_framework import viewsets
from .models import Attachment
from .serializers import AttachmentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

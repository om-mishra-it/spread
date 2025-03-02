from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('-created_at')
    serializer_class = DocumentSerializer

    def create(self, request, *args, **kwargs):
        content = request.data.get("content", "").strip()
        file = request.FILES.get("file")

        if not content and not file:
            return Response({"error": "Either content or file must be provided."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            doc = serializer.save()
            return Response({"message": "Document uploaded successfully", "id": doc.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        documents = self.get_queryset()
        serializer = self.get_serializer(documents, many=True)
        return Response(serializer.data)

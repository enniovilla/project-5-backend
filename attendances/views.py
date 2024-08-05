from rest_framework import generics, permissions
from connectify_api.permissions import IsOwnerOrReadOnly
from attendances.models import Attendance
from attendances.serializers import AttendanceSerializer


class AttendanceList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttendanceDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()

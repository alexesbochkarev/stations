from rest_framework import generics
from .serializers import StationSerializer
from .models import Station


class StationListView(generics.ListAPIView):
    serializer_class = StationSerializer
    queryset = Station.objects.all()


class StationDetailView(generics.RetrieveAPIView):
    serializer_class = StationSerializer
    queryset = Station.objects.all()



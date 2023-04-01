from rest_framework import generics
from .serializers import StationSerializer, TrackSerializer
from .models import Station, Track


class StationListView(generics.ListAPIView):
    serializer_class = StationSerializer
    queryset = Station.objects.filter(active=True)


class StationDetailView(generics.RetrieveAPIView):
    serializer_class = StationSerializer
    queryset = Station.objects.all()


class TracksListView(generics.ListAPIView):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class TrackDetailView(generics.RetrieveAPIView):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
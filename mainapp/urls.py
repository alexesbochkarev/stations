from django.urls import path
from . import views


urlpatterns = [
    path('stations/', views.StationListView.as_view()),
    path('tracks/', views.TracksListView.as_view()),
    path('stations/<int:pk>/', views.StationDetailView.as_view()),
    path('tracks/<int:pk>/', views.TrackDetailView.as_view())
]

from django.urls import path
from . import views


urlpatterns = [
    path('stations/', views.StationListView.as_view()),
    path('stations/<int:pk>/', views.StationDetailView.as_view())
]

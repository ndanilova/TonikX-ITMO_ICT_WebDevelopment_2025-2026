from django.urls import path
from .views import *

app_name = 'parks_app'
urlpatterns = [
    path('enterprises/', EnterpriseListAPIView.as_view()),
    path('services/', ServiceListAPIView.as_view()),
    path('objects/', ObjectListAPIView.as_view()),
    path('contracts/', ContractListAPIView.as_view()),
    path('decorators/', DecoratorListAPIView.as_view()),
    path('objectzones/', ObjectZoneListAPIView.as_view()),
    path('plants/', PlantListAPIView.as_view()),
    path('plantplacements/', PlantPlacementListAPIView.as_view()),
    path('lifeforms/', LifeFormListAPIView.as_view()),
    path('species/', SpeciesListAPIView.as_view()),
    path('plantwateringschedules/', PlantWateringScheduleListAPIView.as_view()),
    path('workers/', WorkerListAPIView.as_view()),
    path('workerassignments/', WorkerAssignmentListAPIView.as_view()),
]

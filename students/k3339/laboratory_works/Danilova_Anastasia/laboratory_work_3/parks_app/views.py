from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


# Create your views here.

class EnterpriseListAPIView(generics.ListAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

class ServiceListAPIView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class ObjectListAPIView(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

class ContractListAPIView(generics.ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class DecoratorListAPIView(generics.ListAPIView):
    queryset = Decorator.objects.all()
    serializer_class = DecoratorSerializer

class ObjectZoneListAPIView(generics.ListAPIView):
    queryset = ObjectZone.objects.all()
    serializer_class = ObjectZoneSerializer

class PlantListAPIView(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantPlacementListAPIView(generics.ListAPIView):
    queryset = PlantPlacement.objects.all()
    serializer_class = PlantPlacementSerializer

class LifeFormListAPIView(generics.ListAPIView):
    queryset = LifeForm.objects.all()
    serializer_class = LifeFormSerializer

class SpeciesListAPIView(generics.ListAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class PlantWateringScheduleListAPIView(generics.ListAPIView):
    queryset = PlantWateringSchedule.objects.all()
    serializer_class = PlantWateringScheduleSerializer

class WorkerListAPIView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerAssignmentListAPIView(generics.ListAPIView):
    queryset = PlantWorkerAssignment.objects.all()
    serializer_class = PlantWorkerAssignmentSerializer


from django.shortcuts import render
from .import models
from .import serializers 
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework.filters import SearchFilter

class  NeighborhoodView(ListAPIView):
    queryset = models.Neighborhood.objects.all()
    serializer_class = serializers.NegihborhoodSerializers
    filter_backends = [SearchFilter]
    search_fields = ['title']
    
class HouseView(ListAPIView):

    queryset = models.House.objects.all()
    serializer_class = serializers.HouseSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['neighborhood','a_b']
    search_fields = ['house_number']
            


class NeighborhoodDetaillView(ListAPIView):
    def get(self, request, id):
        model = models.Neighborhood.objects.get(id=id)
        serializer = serializers.NegihborhoodDetailSerializers(model)
        return Response(serializer.data)
        

class HouseDetailView(ListAPIView):
    def get(self, request, id):
        model = models.House.objects.get(id=id)
        serializer = serializers.HouseDetailSerializer(model)
        return Response(serializer.data)
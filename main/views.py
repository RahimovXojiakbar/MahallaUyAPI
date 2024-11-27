from django.shortcuts import render
from .import models
from .import serializers 
from rest_framework.views import APIView
from rest_framework.response import Response

class  NeighborhoodView(APIView):
    def get(self,request,format=None):
        model = models.Neighborhood.objects.all()
        serializer = serializers.NegihborhoodSerializers(model,  many  =True)
        return Response(serializer.data)
    
class HouseView(APIView):
    def get(self, request, format = None):
        model = models.House.objects.all()
        serializer = serializers.HouseSerializers(model, many=True)
        return Response(serializer.data)
    

class NeighborhoodDetaillView(APIView):
    def get(self, request, id):
        model = models.Neighborhood.objects.get(id=id)
        serializer = serializers.NegihborhoodDetailSerializers(model)
        return Response(serializer.data)
        

class HouseDetailView(APIView):
    def get(self, request, id):
        model = models.House.objects.get(id=id)
        serializer = serializers.HouseDetailSerializer(model)
        return Response(serializer.data)
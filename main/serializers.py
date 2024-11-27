from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .import models 


class NegihborhoodSerializers(ModelSerializer):
    class Meta:
        model = models.Neighborhood
        fields = ['id' ,'title']

class HouseSerializers(ModelSerializer):
    neighborhood = SlugRelatedField(slug_field = 'title', read_only = True)
    class Meta:
        model = models.House
        fields = ['house_number', 'neighborhood']

class NegihborhoodDetailSerializers(ModelSerializer):
    class Meta:
        model = models.Neighborhood
        fields = '__all__'


class HouseDetailSerializer(ModelSerializer):
    neighborhood = SlugRelatedField(slug_field = 'title', read_only = True)
    class Meta:
        model = models.House
        fields = '__all__'
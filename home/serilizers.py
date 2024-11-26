from rest_framework import serializers
from .models import people, Transations
class PersonSerilizers(serializers.ModelSerializer):
    class Meta:
        model=people
        fields= '__all__'



class TransationsSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Transations
        fields=
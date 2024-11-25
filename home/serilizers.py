from rest_framework import serializers
from .models import people
class PersonSerilizers(serializers.ModelSerializer):
    class Meta:
        model=people
        fields= '__all__'
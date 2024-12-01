from rest_framework import serializers
from .models import people, Transactions
class PersonSerilizers(serializers.ModelSerializer):
    class Meta:
        model=people
        fields= '__all__'



class TransactionsSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields='__all__'
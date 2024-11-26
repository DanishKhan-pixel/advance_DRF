from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import people
from .serilizers import PersonSerilizers
# Create your views here.

@api_view(['GET'])
def get_person(request):
    # person={'person_age': 22 , 'person_name': 'ali'}
    person = people.objects.all()
    serilizer = PersonSerilizers(person, many=True)
    return Response({

        'status' : 200,
        'data': serilizer.data
    })

@api_view(['POST'])
def save_data(request):
    data=request.data
    serilizer= PersonSerilizers(data=data)
    if serilizer.is_valid():
        serilizer.save()
        return Response({
            'status':200,
            'data': serilizer.data,
            'massage'  : 'data save successfully '
        })
    
    return Response({

        'status': 400,
        'data' : serilizer.errors,
        'massage' :'some thing wronge'
        
    })




def get_trasantions(request):
     trans= Transations.objects.all()

     return response()
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import people, Transactions
from .serilizers import PersonSerilizers,TransactionsSerilizers
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





# @api_view()
# def get_transactions(request):
#     transactions = Transactions.objects.all()   
#     serializer = TransactionsSerilizers(transactions, many=True)  
#     return Response({
#         "data": serializer.data 
#     })

# @api_view(['POST'])
# def save_transactions(request):
#     data=request.data
#     serializer=TransactionsSerilizers(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({
#             "status" : 200,
#             "data" :serializer.data,
#             "massage": 'your data save successfully  now '
#         })




# Function-Based View Handling Both GET and POST

# @api_view(['GET', 'POST'])
# def transactions(request):
#     if request.method == 'GET':
#         # Handle GET request: Return all transactions
#         transactions = Transactions.objects.all()
#         serializer = TransactionsSerilizers(transactions, many=True)
#         return Response({
#             "data": serializer.data
#         })
#     elif request.method == 'POST':
#         # Handle POST request: Save a new transaction
#         data = request.data
#         serializer = TransactionsSerilizers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "status": 200,
#                 "data": serializer.data,
#                 "message": "Your data was saved successfully."
#             })
#         return Response(serializer.errors, status=400)




# Class-Based View Handling Both GET and POST


class TransactionsView(APIView):
    def get(self, request):
        # Handle GET request: Return all transactions
        transactions = Transactions.objects.all()
        serializer = TransactionsSerilizers(transactions, many=True)
        return Response({
            "data": serializer.data
        })

    def post(self, request):
        # Handle POST request: Save a new transaction
        data = request.data
        serializer = TransactionsSerilizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 200,
                "data": serializer.data,
                "message": "Your data was saved successfully."
            })
        return Response(serializer.errors, status=400)
from django.urls import path
from .views import *

urlpatterns = [
    path('get-person/', get_person),
    path('save-person/', save_data),
    path('transactions/', transactions, name='transactions') #function-based view (@api_view)
    # path('transactions/', TransactionsView.as_view(), name='transactions')  #class-based view (APIView)



]

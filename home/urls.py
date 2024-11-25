from django.urls import path
from .views import *

urlpatterns = [
    path('get-person/', get_person),
    path('save-person/', save_data)


]

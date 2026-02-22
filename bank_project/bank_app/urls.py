from django.urls import path
from .views import BankPredict

urlpatterns = [
    path('predict/', BankPredict.as_view(), name='bank_predict')
]
from rest_framework.viewsets import ModelViewSet
from .models import Expense
from .serializers import ExpenseSerializer
from django.http import JsonResponse
from .ml_model import predict_expense

class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

def predict(request):
    amount = float(request.GET.get('amount', 0))
    predicted_value = predict_expense(amount)
    return JsonResponse({'predicted_expense': predicted_value})

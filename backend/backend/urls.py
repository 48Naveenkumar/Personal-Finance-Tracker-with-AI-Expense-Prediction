from rest_framework.routers import DefaultRouter
from expenses.views import ExpenseViewSet

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = router.urls

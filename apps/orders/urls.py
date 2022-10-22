from django.urls import path
from . import views

urlpatterns = [
    path('order-create/', views.OrderCreateAPIView.as_view()),
    path('card-create/', views.CardCreate.as_view()),
    path('verify-phone/', views.CardVerify.as_view()),
    path('payment/', views.ReceiptCreate.as_view())
]

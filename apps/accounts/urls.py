from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('verify-register/', views.VerifyPhoneRegisterAPIView.as_view()),
    path('verify-login/', views.VerifyPhoneAPIView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('add-connection/', views.AddConnectionAPIView.as_view()),
    path('rud-myaccount/<int:pk>/', views.MyAccountRUDAPIView.as_view())
]

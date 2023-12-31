from rest_framework import routers
from django.urls import path, include
from . import views

# router = routers.DefaultRouter()
# router.register(r'', views.generate_token)

urlpatterns = [
    path('gettoken/<str:id>/<str:token>/', views.generate_token, name='token.generate'),
    path('process/<str:id>/<str:token>/', views.process_payment, name='payment.process'),
]

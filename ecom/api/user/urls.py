from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewsSet)

urlpatterns = [
    path('login/',views.signin, name='signin'),
    path('logout/'views.signout, Name='signout')
]

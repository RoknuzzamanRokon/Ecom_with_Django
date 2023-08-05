from rest_framework import viewsets
from .serializers import UserSerializer
from .models import CustomUser

# Generate a Random number.
import random

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length))



# Create your views here.
class UserViewsSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('something')
    serializer_class = UserSerializer
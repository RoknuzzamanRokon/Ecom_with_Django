from rest_framework import viewsets,permissions
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import re
from .serializers import UserSerializer
from .models import CustomUser



# Generate a Random number.
import random
def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length))


@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameter only'})
   
# Extract Username and Password from Request.  
    username = request.POST['email']
    password = request.POST['password']
    
# Validation Part.
    # Check email validation part.
    if not re.match('([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}', username):
        return JsonResponse({'error': 'Enter a valid email'})
    
    # Check password validation part.
    if len(password) < 3:
        return JsonResponse({'error': 'Password needs to be at last of 3 character'})
    
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(email=username)
        
        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password')
            
            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': "Previous session exists"})
            
            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request=request, user=user)
            return JsonResponse({'token': token, 'user': usr_dict})
        else:
            return JsonResponse({'error': "Invalid password"})
              
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid Email'})
    
    
# def signout(request):
#     if request.user.is_authenticated:
#         user = request.user
#         user.session_token = "0"  # Set the session token to "0" to invalidate it
#         user.save()
#         logout(request)  # Log the user out
#         return JsonResponse({'message': 'Logout successful'})
#     else:
#         return JsonResponse({'error': 'User is not authenticated'})
    
def signout(request,id):
    logout(request)
    
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
        
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})
    
    return JsonResponse({'Success': 'Logout Success'})
        
        
        
        
        
# Create your views here.
class UserViewsSet(viewsets.ModelViewSet):
    
    permission_classes_by_action = {'create': [AllowAny]}
    
    queryset = CustomUser.objects.all().order_by('sid')
    serializer_class = UserSerializer
    
    def get_permissions(self):
        try:
            return [permissions.AllowAny() for permissoin in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions.AllowAny() for permissoin in self.permission_classes]
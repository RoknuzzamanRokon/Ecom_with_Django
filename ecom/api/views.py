from django.http import JsonResponse


# Create your views here.
def home(request):
    """Api views."""
    return JsonResponse({'info': 'Django React Course', 'name': "ROko"})


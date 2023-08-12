from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model


# Create your views here.
import braintree


gateway = braintree.BraintreeGateway(
  braintree.Configuration(
      braintree.Environment.Sandbox,
      merchant_id="6nkm3txth47zjd9b",
      public_key="p28mw28gjztk67xb",
      private_key="433fe482b4553d74261c8f437a6a3332"
  )
)


def validate_user_session(id, token):
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False
    
# Generate token session area.
@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token=token):
        return JsonResponse({'error': 'Invalid session'})
    
    return JsonResponse({'clientToken': gateway.client_token.generate(),'success': True})
    
    
@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token=token):
        return JsonResponse({'error': 'Invalid session'})
    
    nonce_from_the_client = request.POST["payment_method_Nonce"]
    amount_from_the_client = request.POST['Amount']
    
    result = gateway.transaction.sale({
    "amount": amount_from_the_client,
    "payment_method_nonce": nonce_from_the_client,
    "options": {
      "submit_for_settlement": True
    }
    })
    
    if result.is_success:
        return JsonResponse({"success": result.is_success,
                             "transaction":{"id":result.transaction.id, "amount": result.transaction.amount}})
    else:
        return JsonResponse({'error':True, 'success':False})
    
    
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from jonjo.models import Subcategory
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "cart_summary.html", {"cart_products":cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')  # Match the frontend key
        if not product_id:
            return JsonResponse({'error': 'Product ID not provided'}, status=400)

        try:
            product_id = int(product_id)
        except ValueError:
            return JsonResponse({'error': 'Invalid Product ID'}, status=400)

        product = get_object_or_404(Subcategory, id=product_id)
        cart.add(product=product)
        
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response
 
      
def cart_delete(request):
    pass

def cart_update(request):
    pass
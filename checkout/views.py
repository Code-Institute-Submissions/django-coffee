from django.shortcuts import render, reverse, HttpResponse, get_object_or_404

#import settings so that we can access the public stripe key
from django.conf import settings
import stripe

from catalog.models import Product

# Create your views here.
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    # retrieve shopping cart
    cart = request.session.get('shopping_cart', {})
    
    line_items = []
    
    # generate the line_items
    for id, product in cart.items():
        # For each item in the cart, get its details from the database
        product = get_object_or_404(Product, pk=id)
        line_items.append({
            'name': product.name,
            'amount': int(product.price*100), #convert to cents, in integer
            'currency':'sgd',
            'quantity':1
        })
    
    #generate the session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=request.build_absolute_uri(reverse(checkout_success)),
        cancel_url=request.build_absolute_uri(reverse(checkout_cancelled)),
    )
    
    # render the template
    return render(request, 'checkout/checkout.template.html', {
        'session_id':session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })
    
def checkout_success(request):
    # Empty the shopping cart
    request.session['shopping_cart'] = {}
    return HttpResponse("Checkout success")
    
def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")
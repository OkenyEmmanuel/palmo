from jonjo.models import Subcategory

class Cart:
    def __init__(self, request):
        """
        Initialize the cart with the session.
        If the cart doesn't exist in the session, create it.
        """
        self.session = request.session
        # Retrieve the cart from the session or initialize an empty dictionary
        cart = self.session.get('session_key')
        if cart is None:
            cart = self.session['session_key'] = {}
        self.cart = cart  # Ensure self.cart is always a dictionary

    def add(self, product):
        """
        Add a product to the cart or update its details if already in the cart.
        """
        product_id = str(product.id)  # Convert the product ID to a string
        if product_id in self.cart:
            # Update logic can go here, e.g., incrementing quantity
            pass
        else:
            # Add product details to the cart
            self.cart[product_id] = {'price': str(product.price)}
        # Mark the session as modified to ensure changes are saved
        self.session.modified = True
        
        
    def __len__(self):
        return len(self.cart)  
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Subcategory.objects.filter(id__in=product_ids)      
        return products
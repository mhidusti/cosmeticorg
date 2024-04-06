from .models import Products
class Wish:
    def __init__(self, request):
        """
        Construct a wish
        """
        self.request = request
        self.session = request.session
        wish = self.session.get('wish')
        if wish is None:
            wish = self.session['wish'] = {}
        self.wish = wish

    def save(self):
        """
        Update the wish
        """
        self.session.modified = True

    def add_to_wish_some_quantity(self, product, quantity=1):
        """"
        Add a product to the wish over than 1
        """
        if str(product.id) not in self.wish:
            self.wish[str(product.id)] = {'quantity': quantity}

        else:
            self.wish[str(product.id)]['quantity'] += quantity
        

        self.save()

    def add_to_wish_one_quantity(self, product):
        """"
        Add a product to the wish just one quantity
        """

        if str(product.id) not in self.wish:
            self.wish[str(product.id)] = {'quantity': 1}

        self.save()

    def delete_from_wish(self,product):
        """
        Delete a product from the
        """

        if str(product.id) in self.wish:
            del self.wish[str(product.id)]
            self.save()

    def __iter__(self):
        """
        Iterate over all products
        """
        product_ids = self.wish.keys()
        products = Products.objects.filter(id__in=product_ids)
        wish = self.wish.copy()#generator empty list . use copy for keep base wish
        for product in products:
            wish[str(product.id)]['product_object'] = product

        for item in wish.values():
            yield item

    def __len__(self):
        """
        Returns the lenght of wish objects
        """
        return len(self.wish.keys())
    
    def clear(self):
        """
        Clear all products
        """
        del self.session['wish']
        self.save()

    
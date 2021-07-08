from django.shortcuts import render
from django.views import generic
from .models import *


class ProductListView(generic.ListView):
    model = Category
    template_name = "jobapplication/list.html"
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "jobapplication/detail.html"


class AddToCartView(generic.TemplateView):
    template_name = 'jobapplication/tocart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # id from requested url
        product_id = self.kwargs['pro_id']

        # get product
        product_obj = Product.objects.get(id=product_id)


        # check if cart exist
        cart_id = self.request.session.get("cart_id", None)

        # if cart exists
        if cart_id:
            cart_obj  = Cart.objects.get(id=cart_id)
            
            this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)

            # for item exists in cart
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.selling_price
                cartproduct.save()
                cart_obj.total += product_obj.selling_price
                cart_obj.save()
            
            # new item in cart
            else:
                cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.selling_price,
                quantity=1, subtotal=product_obj.selling_price
                )
                
                cart_obj.total += product_obj.selling_price
                cart_obj.save()

        
        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            print('old cart')
            cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.selling_price,
                quantity=1, subtotal=product_obj.selling_price
            )
            
            cart_obj.total += product_obj.selling_price
            cart_obj.save()

        return context


class MyCartView(generic.TemplateView):
    template_name = 'my-carts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)

        if cart_id:
            cart = Cart.objects.get(id=cart_id)

        else:
            cart = None
        
        context['cart'] = cart
        return context




        return context
    
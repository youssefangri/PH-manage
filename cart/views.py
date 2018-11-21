from django.shortcuts import render,redirect


from Medicament.models import Medicament
from .models import Cart
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {})

def cart_update(request):
    med_id = request.POST.get("selected_Med_button")
    print(med_id)
    if med_id is not None:
        try:
            med_obj = Medicament.objects.get(id=med_id)
        except Medicament.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("/")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if med_obj in cart_obj.Medicaments.all():
            cart_obj.Medicaments.remove(med_obj)
            added = False
        else:
            cart_obj.Medicaments.add(med_obj) # cart_obj.products.add(product_id)
            added = True
    return redirect("/")

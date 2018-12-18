from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Command
from cart.models import Cart
from Medicament.models import Medicament


def checkout(request):
    try:
        cart_obj = Cart.objects.get(id=request.POST.get("checkout_button"))
        med_select = cart_obj.Medicaments.all()
    except:
        raise Http404("Not found..")
    try:
        M = Command.objects.create()
        M.user = cart_obj.user
        for med in med_select:
            M.Medicaments.add(med)

        M.subtotal = cart_obj.subtotal
        M.total = cart_obj.total
        M.Comment = request.POST.get("Comment")
        M.save()
        #substrac quantity
        content = {}
        for med in med_select:
            try:
                med.quantity = (med.quantity)-1
                if med.quantity < 0:
                    content["status"]="error quantity"
                else:
                    med.save()
                    content["status"]="success"
            except:
                content["status"]="error"
                pass
        #delet session to create another
        cart_obj.delete()
    except:
        print ("error")
    return redirect("/")

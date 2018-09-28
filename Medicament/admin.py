from django.contrib import admin

from .models import Medicament

class MedicamentAdmin(admin.ModelAdmin):
    list_display =  ['__str__', 'price', 'quantity']
    class Meta:
        model = Medicament

admin.site.register(Medicament, MedicamentAdmin)

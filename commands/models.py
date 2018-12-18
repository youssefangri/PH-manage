from decimal import Decimal
from django.conf import settings
from django.db import models
#from django.db.models.signals import pre_save, post_save, m2m_changed

from cart.models import Cart
from Medicament.models import Medicament
User = settings.AUTH_USER_MODEL

class CustomManager(models.Manager):

	def get_queryset(self):
		super_query = super(models.Manager,self).get_queryset()
		return super_query



class Command(models.Model):
	user			= models.ForeignKey(User, null=True, blank=True)
	Medicaments		= models.ManyToManyField(Medicament, blank=True)
	Comment			= models.CharField(max_length=120, blank=True, null=True)
	subtotal		= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	total			= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	timestamp		= models.DateTimeField(auto_now_add=True)

	objects = CustomManager()
	def save(self, *args, **kwargs):
		super(Command, self).save(*args, **kwargs)
	def __str__(self):
		return str(self.id)

from django.db import models


# Create your models here.

class CustomManager(models.Manager):
	
	def get_queryset(self):
		super_query = super(models.Manager,self).get_queryset()
		return super_query
		

class Medicament(models.Model):
	title 		= models.CharField(max_length=120)
	price 		= models.DecimalField(decimal_places=2, max_digits=20, null=False)
	quantity 	= models.PositiveIntegerField()
	
	objects = CustomManager()
	
	def save(self, *args, **kwargs):
		super(Medicament, self).save(*args, **kwargs)
	def __str__(self):
		return self.title

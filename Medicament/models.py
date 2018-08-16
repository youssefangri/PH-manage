from django.db import models

# Create your models here.

class Medicament(models.Model):
	title 		= models.CharField(max_length=120)
	price 		= models.DecimalField(decimal_places=2, max_digits=20, null=False)
	quantity 	= models.PositiveIntegerField()
	
	def __str__(self):
		return self.title

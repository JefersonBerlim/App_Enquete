from django.db import models

# Create your models here.

class Enquete(models.Model):
	nome = models.CharField( max_length = 40, null=False )
	email = models.TextField(null=False )
	HTML = models.CharField(max_length=1, null=True )
	CSS = models.CharField(max_length=1, null=True )
	Javascript = models.CharField(max_length=1, null=True )
	Python = models.CharField(max_length=1, null=True )
	Django = models.CharField(max_length=1, null=True )
	Desenv_IOS = models.CharField(max_length=1, null=True )
	Desenv_Android = models.CharField(max_length=1, null=True )

	def __unicode__(self):
		return self.nome
from django.db import models

# Create your models here.

class Plot(models.Model):
	image = models.FileField()

	def delete(self, *args, **kwargs):
		self.image.delete()
		super(Plot, self).delete(*args, **kwargs)
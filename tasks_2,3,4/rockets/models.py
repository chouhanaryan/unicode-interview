from django.db import models
from django.urls import reverse

class RocketLaunch(models.Model):
	flight_number = models.IntegerField()
	# time = models.CharField(max_length=50, default=-1)
	launch_date_time = models.DateTimeField(null=True, blank=True)
	name = models.CharField(max_length=50)
	link = models.ImageField(null=True)
	# id = models.IntegerField(primary_key=True)

	def get_absolute_url(self):
		"""Returns the url to access a particular author instance."""
		return reverse('rocketlaunch-detail', args=[str(self.id)])

	def __str__(self):		
		"""String for representing the Model object."""
		return f'({self.flight_number}, {self.name})'
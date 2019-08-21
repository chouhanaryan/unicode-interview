from django.db import models
from django.urls import reverse

class RocketLaunch(models.Model):
	flight_number = models.IntegerField()
	# time = models.CharField(max_length=50, default=-1)
	launch_date_time = models.DateTimeField(null=True, blank=True)
	name = models.CharField(max_length=50)
	link = models.ImageField(null=True)
	launch_success = models.BooleanField(null=True, blank=True)
	youtube_id = models.CharField(max_length=50, blank=True, null=True)
	wikipedia_link = models.CharField(max_length=100, blank=True, null=True)
	site_name = models.CharField(max_length=100, blank=True, null=True)	

	def get_absolute_url(self):
		# Returns the url to access a particular launch instance
		return reverse('rocketlaunch-detail', args=[str(self.id)])

	def __str__(self):		
		# String for representing the Model object
		return f'({self.flight_number}, {self.name})'

	class Meta:
		verbose_name_plural = "Rocket launches"
		verbose_name = "Rocket launch"
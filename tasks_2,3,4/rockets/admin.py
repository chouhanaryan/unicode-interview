from django.contrib import admin
from rockets.models import RocketLaunch
# Register your models here.


class RocketLaunchAdmin(admin.ModelAdmin):
	list_display = ('name', 'flight_number')
	fields = ['name', 'flight_number', 'launch_date_time', 'link']

admin.site.register(RocketLaunch,RocketLaunchAdmin)
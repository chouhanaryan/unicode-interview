from django.contrib import admin
from rockets.models import RocketLaunch
# Register your models here.


class RocketLaunchAdmin(admin.ModelAdmin):
	list_display = ('name', 'flight_number')
	fields = ['name', 'flight_number', 'launch_date_time', 'link', 'launch_success', 'site_name', 'youtube_id', 'wikipedia_link']
	list_filter = ['launch_success', 'site_name']


admin.site.register(RocketLaunch, RocketLaunchAdmin)
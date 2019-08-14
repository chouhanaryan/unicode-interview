from django.shortcuts import render
from rockets import models
from django.views import generic
import requests
import datetime

def index(request):
	rockets_count = models.RocketLaunch.objects.all().count()

	return render (request, 'index.html', {'rockets_count': rockets_count})

def load(request):
	if models.RocketLaunch.objects.all().count() != 101:

		url = 'https://api.spacexdata.com/v3/launches'	
		response = requests.get(url).json()		
		for rocket in response:
			r = models.RocketLaunch()
			r.flight_number = rocket['flight_number']
			x = rocket['launch_date_utc'][:10]
			y = rocket['launch_date_utc'][11:22]
			z = x+' '+y
			r.launch_date_time = datetime.datetime.strptime(z, '%Y-%m-%d %H:%M:%S.%f')
			r.name = rocket['mission_name']
			r.link = rocket['links']['mission_patch_small']
			r.wikipedia_link = rocket['links']['wikipedia']
			r.youtube_id = rocket['links']['youtube_id']
			s = models.SiteName()
			s.site_name = rocket['launch_site']['site_name']
			# r.site_name = s
			r.launch_success = rocket['launch_success']
			# s.save()
			r.save()

		return render(request, 'load_success.html')

	else:

		return render(request, 'load_failure.html')

def flush(request):
	models.RocketLaunch.objects.all().delete()

	return render(request, 'flush.html')

def launch_list(request):
	rockets = models.RocketLaunch.objects.all()
	# paginator = Paginator(rockets_all, 10)
	# page = request.GET.get('page')
	# rockets = paginator.get_page(page)  
	return render(request, 'launch_list.html', {'rockets': rockets})

class RocketLaunchDetailView(generic.DetailView):
	model = models.RocketLaunch

class SiteNameListView(generic.ListView):
	model = models.SiteName
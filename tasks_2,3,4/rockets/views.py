from django.shortcuts import render
from rockets import models
from django.views import generic
import requests
import datetime
# from django.utils.timezone import make_aware
# import pytz


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
			# make_aware(dt, timezone=pytz.timezone("UTC"))			 
			r.name = rocket['mission_name']
			r.link = rocket['links']['mission_patch_small']
			r.wikipedia_link = rocket['links']['wikipedia']
			r.youtube_id = rocket['links']['youtube_id']
			r.site_name = rocket['launch_site']['site_name']
			r.launch_success = rocket['launch_success']
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

def handler404(request, exception):
	return render(request, '404.html', status=404)

def handler500(request):
	return render(request, '500.html', status=500)
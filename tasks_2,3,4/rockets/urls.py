from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('launches/', views.launch_list, name='launch-list'),
    path('launches/<int:pk>', views.RocketLaunchDetailView.as_view(), name='rocketlaunch-detail'),
	path('load/', views.load, name='load'),
	path('flush/', views.flush, name='flush')
]

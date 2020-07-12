from django.urls import path
from .views import home,about,services,contacts,country,economic,politics,science,startup


app_name = 'pages'

urlpatterns = [
	path('',home,name='home'),
	path('about/',about,name='about'),
	path('servies/',services,name='services'),
	path('contacts/',contacts,name='contacts'),
	path('country/',country,name='country'),
	path('economic/',economic,name='economic'),
	path('politics/',politics,name='politics'),
	path('science/',science,name='science'),
	path('startup/',startup,name='startup'),

]
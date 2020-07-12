from django.shortcuts import render

# Create your views here.

def home(request):

	return render(request,'home.html')


def about(request):

	return render(request,'about.html')

def services(request):

	return render(request,'services.html')

def contacts(request):

	return render(request,'contacts.html')

def country(request):

	return render(request,'country.html')

def economic(request):

	return render(request,'economic.html')

def politics(request):

	return render(request,'politics.html')

def startup(request):

	return render(request,'startup.html')

def science(request):

	return render(request,'science.html')
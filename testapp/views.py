from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Person
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    return HttpResponse("Test Application")

def employees(request):
	person_list = Person.objects.all()
	paginator = Paginator(person_list, 3)
	page = request.GET.get('page')
	try:
	    persons = paginator.page(page)
	except PageNotAnInteger:
	    persons = paginator.page(1)
	except EmptyPage:
	    persons = paginator.page(paginator.num_pages)
	return render(request, 'employees.html', {'person_list': persons})
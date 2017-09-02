from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Person
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from .forms import DepartmentForm
# Create your views here.

def index(request):
    return HttpResponse("Test Application")

def employees(request):
	form = DepartmentForm()
	person_list = Person.objects.all()
	paginator = Paginator(person_list, 3)
	page = request.GET.get('page')
	try:
	    persons = paginator.page(page)
	except PageNotAnInteger:
	    persons = paginator.page(1)
	except EmptyPage:
	    persons = paginator.page(paginator.num_pages)
	return render(request, 'employees.html', {'person_list': persons, 'form': form})

class PersonListView(generic.ListView):
	template_name = 'people.html'
	context_object_name = 'person_list'
	paginate_by = 2
	def get_queryset(self):
		person_list = Person.objects.all()
		if self.request.GET.get('department'):
			department_val = self.request.GET.get('department')
#			person_list = Person.objects.filter(department = 2)
			person_list = person_list.filter(
				department = department_val,
			)
		if self.request.GET.get('retire'):
			retire_val = self.request.GET.get('retire')
			person_list = person_list.filter(
				retireDate = retire_val,
			)
		'''
		form = DepartmentForm()
		if form.is_valid():
			person_list = Person.objects.filter(name = "Vladimir")
		else:
			person_list = Person.objects.all()
#		return Person.objects.all()
'''
		return person_list
	def get_context_data(self, **kwargs):
		context = super(PersonListView, self).get_context_data(**kwargs)
		context['form'] = DepartmentForm()
		return context
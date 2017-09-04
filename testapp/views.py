from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Person
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from .forms import DepartmentForm
# Create your views here.


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def index(request):
	return render(request, 'index.html')
    #return HttpResponse("Test Application")

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

class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'person.html'
    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        return context

def alphalist(request):
	letters = list()
	firstletter = 'a'
	person_list = Person.objects.order_by('sirname')
	p_count = person_list.count()
	chunk_list = list(chunks(person_list, p_count//7+1))
	for people in chunk_list:
		sirname = people[len(people)-1].sirname
		letters.append(firstletter+'-'+sirname[0])
		firstletter = chr(ord(sirname[0])+1)
	print(letters)

	if request.method == "POST":
		post_letters = request.POST.get("letters", "")
		post_letters = '['+post_letters.lower()+post_letters.upper()+']%%'
		print("HelloPost")
		print(post_letters)
		#person_list = Person.objects.extra(where=["sirname SIMILAR TO '[a-zA-Z]%%'"])
		person_list = Person.objects.extra(where=["sirname SIMILAR TO %s"], params=[post_letters])
	return render(request, 'alpha.html', {'person_list': person_list, 'letters': letters})

class AlphaListView(generic.ListView):
	template_name = 'alpha.html'
	context_object_name = 'person_list'
	
	def get_queryset(self):
		person_list = Person.objects.order_by('sirname')

		if self.request.method == "POST":
			post_letters = self.request.POST.get("letters", "")
			post_letters = '['+post_letters.lower()+post_letters.upper()+']%%'
			print("HelloPost")
			print(post_letters)
			#person_list = Person.objects.extra(where=["sirname SIMILAR TO '[a-zA-Z]%%'"])
			person_list = Person.objects.extra(where=["sirname SIMILAR TO %s"], params=[post_letters])
		return person_list
	def get_context_data(self, **kwargs):
		context = super(AlphaListView, self).get_context_data(**kwargs)
		letters = list()
		firstletter = 'a'
		person_list = Person.objects.order_by('sirname')
		p_count = person_list.count
		chunk_list = list(chunks(person_list, 2))
		for people in chunk_list:
			sirname = people[len(people)-1].sirname
			letters.append(firstletter+'-'+sirname[0])
			firstletter = chr(ord(sirname[0])+1)
		print(letters)
		context['letters'] = letters
		return context

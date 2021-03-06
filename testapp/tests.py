from django.test import TestCase
from django.test.client import Client
from .models import Department, Person
import datetime

# Create your tests here.

class SimpleTest(TestCase):
	def setUp(self):
		self.client = Client()

	def test_listView(self):
		response = self.client.get('/testapp/people/')
		self.assertEqual(response.status_code, 200)

	def test_detailView(self):
		response = self.client.get('/testapp/person/1')
		self.assertEqual(response.status_code, 404)
		now = datetime.datetime.now()
		department = Department.objects.create(name='foo', creation_date=now)
		person = Person.objects.create(name='foo', sirname='bar', patronymic='foobar', birthdate=now, email='foo@bar.ru', employDate=now, occupation = 'occ', department=department)
		#self.assertEqual(Person.objects.get(pk=person.id).id, 1)
		response = self.client.get('/testapp/person/'+str(person.id))
		self.assertEqual(response.status_code, 200)

class ModelsTest(TestCase):
    def test_my_test_model(self):
    	now = datetime.datetime.now()
        self.assertTrue(Department.objects.create(name='foo', creation_date=now))
        department = Department.objects.create(name='foo', creation_date=now)
        self.assertTrue(Person.objects.create(name='foo', sirname='bar', patronymic='foobar', birthdate=now, email='foo@bar.ru', employDate=now, occupation = 'occ', department=department))

class AlphaTest(TestCase):
	def setUp(self):
		self.client = Client()
	def test_alphaView(self):
		response = self.client.get('/testapp/alpha/')
		self.assertEqual(response.status_code, 200)
	def test_alphaFilter(self):
		now = datetime.datetime.now()
		department = Department.objects.create(name='foo', creation_date=now)
		self.assertTrue(Person.objects.create(name='foo', sirname='bar', patronymic='foobar', birthdate=now, email='foo@bar.ru', employDate=now, occupation = 'occ', department=department))
		self.assertTrue(Person.objects.create(name='goo', sirname='gar', patronymic='foobar', birthdate=now, email='foo@bar.ru', employDate=now, occupation = 'occ', department=department))

		response = self.client.get('/testapp/alpha/')
		self.assertContains( response, '<input name = "letters" type = "hidden" value = "a-b" />', status_code=200 )
		self.assertContains( response, '<input name = "letters" type = "hidden" value = "c-g" />', status_code=200 )
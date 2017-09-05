from django.db import models

# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length=100)
	creation_date = models.DateTimeField('date created')
	
	def __unicode__(self):
		return u'%s' % (self.name)


class Person(models.Model):
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	sirname = models.CharField(max_length=50)
	patronymic = models.CharField(max_length=50)
	birthdate = models.DateField(auto_now=False, auto_now_add=False)
	email = models.EmailField(max_length=50)
	employDate = models.DateField('employment date')
	retireDate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	occupation = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s %s' % (self.name, self.sirname)


from django import forms
from .models import Department
from django.contrib.admin.widgets import AdminDateWidget

class DepartmentForm(forms.Form):
	departments = Department.objects.all()
	department = forms.ModelChoiceField(queryset = departments, required = False)
	retire = forms.DateField(widget = AdminDateWidget(),  required = False)
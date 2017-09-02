from django import forms
from .models import Department

class DepartmentForm(forms.Form):
	departments = Department.objects.all()
	department = forms.ModelChoiceField(queryset = departments)
from django import forms
from todo.models import TaskList
from datetime import date
from django.core.exceptions import ValidationError
from django.utils import timezone

class TaskForm(forms.ModelForm):
	class Meta:
		model = TaskList
		fields = ['task','taskDescription','importance','deadline']
		widgets = {
            'task_Assign_Date': forms.DateInput(attrs={'type': 'date'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

	def clean_deadline(self):
		deadline = self.cleaned_data.get('deadline')
		if deadline and deadline < timezone.now().date():
			raise ValidationError('The deadline must be today or in the future.')
		return deadline
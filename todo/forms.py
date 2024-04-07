from django import forms
from todo.models import TaskList
from datetime import date

class TaskForm(forms.ModelForm):
	class Meta:
		model = TaskList
		fields = ['task','taskDescription','importance','deadline']
		widgets = {
            'task_Assign_Date': forms.DateInput(attrs={'type': 'date'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
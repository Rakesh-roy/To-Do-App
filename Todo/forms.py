from django import forms
from Todo.models import TodoModel


class ToDoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'
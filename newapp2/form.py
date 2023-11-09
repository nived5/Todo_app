from django import forms

from newapp2.models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title','description')

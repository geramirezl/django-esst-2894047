from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title','text')
        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text' : forms.Textarea(attrs={'class': 'form-control my-5'})
        }
        labels= {
            'text':'Write your thoughts here '
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        return title
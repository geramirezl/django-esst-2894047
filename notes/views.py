from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView,ListView,DetailView

from .forms import NoteForm
from .models import Notes

class NotesCreateView(CreateView):
    model = Notes 
    success_url = '/smart/notes'
    form_class = NoteForm


class NotesListView(ListView):
    model = Notes 
    context_object_name= "notes"
    template_name="notes/notes_list.html"


class NotesDetailView(DetailView):
    model= Notes
    context_object_name="note"
    template_name="notes/notes_detail.html"


class PopularListViews(ListView):
    model = Notes 
    context_object_name= "notes"
    template_name="notes/notes_list.html"
    queryset= Notes.objects.filter(likes__gte=1)
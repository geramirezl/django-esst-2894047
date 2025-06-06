from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView,ListView,DetailView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import NoteForm
from .models import Notes

def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes +=1
        note.save()
        return HttpResponseRedirect(reverse("notes.detail",args=(pk,)))
    raise Http404


class NotesDeleteView(DeleteView):
    model= Notes
    success_url='/smart/notes'
    template_name="notes/notes_delete.html"

class NotesUpdateView(UpdateView):
    model = Notes 
    success_url = '/smart/notes'
    form_class = NoteForm

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
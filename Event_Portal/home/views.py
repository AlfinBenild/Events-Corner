from django.shortcuts import render
from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView
)

# Create your views here.

def Home(request):
    return render(request, 'home/home.html')

class HomeListView(ListView):
    model = Event
    template_name = 'home/events.html'
    context_object_name = 'events'
    ordering = ['-date_created']

class HomeDetailView(DetailView):
    model = Event
    
class HomeCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'date', 'time', 'location', 'max_no', 'banner']

    def form_valid(self, form):
        form.instance.person_created = self.request.user
        return super().form_valid(form)

class HomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'date', 'time', 'location', 'max_no', 'banner']

    def form_valid(self, form):
        form.instance.person_created = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.person_created:
            return True
        return False    

class HomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/events'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.person_created:
            return True
        return False


def events(request):
    context = {
        'events' : Event.objects.all(),
    }
    return render(request, 'home/events.html', context)
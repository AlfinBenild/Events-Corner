from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Register
from django.contrib import messages

# Create your views here.
class RegisterCreateView(LoginRequiredMixin, CreateView):
    model = Register
    success_url = '/'

    fields = ['name', 'email', 'phone', 'branch', 'event']

    def form_valid(self, form):
        form.instance.person_created = self.request.user
        event_list = list(Register.objects.all())
        for item in event_list:
            if (item.person_created.username == form.instance.person_created.username) and (item.event.title == form.cleaned_data['event'].title):
                messages.warning(self.request, f'You have already registered for this event!')
                return self.form_invalid(form)
        messages.success(self.request, f'Successfully registered')
        return super().form_valid(form)
    

from django.shortcuts import render
from AppMaquinas.models import Maquina
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "AppMaquinas/index.html")


class MaquinaList(ListView):
    model = Maquina
    context_object_name= "maquinas" 
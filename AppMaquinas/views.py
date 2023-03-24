from django.shortcuts import render
from AppMaquinas.models import Maquina, Profile, Mensaje
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "AppMaquinas/index.html")

#CRUD Maquinas
class MaquinaList(ListView):
    model = Maquina
    context_object_name= "maquinas" 

#entrar y salir al sistema
class Login(LoginView):
    next_page = reverse_lazy("index")


class Logout(LogoutView):
    template_name = "registration/logout.html"


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('maquina-list')

#crear perfil


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("maquina-list")
    fields = ['avatar']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("maquina-list")
    fields = ['avatar']

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()

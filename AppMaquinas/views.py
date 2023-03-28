from django.shortcuts import render
from AppMaquinas.models import Maquina, Profile, Mensaje
from AppMaquinas.forms import UsuarioForm #Formulario en que agregue campos de apellido y nombre
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

class MaquinaMineList(LoginRequiredMixin, MaquinaList):

    def get_queryset(self):
        return Maquina.objects.filter(propietario=self.request.user.id).all()


class MaquinaDetail(DetailView):
    model = Maquina
    context_object_name = "maquina"


class ValidarId(UserPassesTestMixin):
    def test_func(self):
        user_id = self.request.user.id
        maq_id = self.kwargs.get("pk")
        return Maquina.objects.filter(propietario=user_id, id=maq_id).exists()


class MaquinaUpdate(LoginRequiredMixin, ValidarId, UpdateView):
    model = Maquina
    success_url = reverse_lazy("maquina-list")
    fields = '__all__'

class MaquinaDelete(LoginRequiredMixin, ValidarId, DeleteView):
    model = Maquina
    context_object_name = "maquina"
    success_url = reverse_lazy("maquina-list")


class MaquinaCreate(LoginRequiredMixin, CreateView):
    model = Maquina
    success_url = reverse_lazy("maquina-list")
    fields = ['nombre', 'detalle', "estado", "precio",  "imagen"]

    def form_valid(self, form):
        form.instance.propietario = self.request.user # Obtengo id del usuario y lo guardo en propietario
        return super().form_valid(form)

#Buscar maquina por nombre
class MaquinaSearch(ListView):
    model = Maquina
    context_object_name = "maquinas"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        resultado = Maquina.objects.filter(nombre__icontains=criterio).all()
        return resultado
    
#entrar y salir al sistema
class Login(LoginView):
    next_page = reverse_lazy("index")


class Logout(LogoutView):
    template_name = "registration/logout.html"


class SignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

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

#Mensajeria
class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('maquina-mine')
    fields = '__all__'

class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()


class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb
        pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()


def about(request):
    return render(request, "AppMaquinas/about.html")

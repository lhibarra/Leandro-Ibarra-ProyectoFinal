"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from AppMaquinas.views import (index, MaquinaList, 
Login, Logout, SignUp, ProfileCreate, ProfileUpdate, 
MaquinaMineList, MaquinaUpdate, MaquinaDetail, MaquinaDelete,
MaquinaCreate, MaquinaSearch, MensajeCreate, MensajeDelete, MensajeList,
about
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', about, name="about"),
    #urls maquinas
    path('', index, name="index"),
    path('maquina/list', MaquinaList.as_view(), name="maquina-list"),
    path('maquina/list/mine', MaquinaMineList.as_view(),name="maquina-mine"),
    path('maquina/detail/<pk>/', MaquinaDetail.as_view(), name="maquina-detail"),
    path('maquina/update/<pk>/', MaquinaUpdate.as_view(), name="maquina-update"),
    path('maquina/delete/<pk>/', MaquinaDelete.as_view(), name="maquina-delete"),
    path('maquina/create/', MaquinaCreate.as_view(), name="maquina-create"),
    path('maquina/buscar/', MaquinaSearch.as_view(), name="maquina-buscar"),
    #url ingreso sistema
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('signup/', SignUp.as_view(), name="signup"),
    #urls manejo perfil
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
    path('profile/update/<pk>/', ProfileUpdate.as_view(), name="profile-update"),
    # urls Mensaje
    path('mensaje/create/', MensajeCreate.as_view(), name= "mensaje-create"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('mensaje/delete/<pk>/', MensajeDelete.as_view(), name="mensaje-delete"),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

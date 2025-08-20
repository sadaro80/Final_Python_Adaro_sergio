from django.urls import path
from . import views
from django.contrib.auth.views import LoginView




urlpatterns = [
    path('', views.inicioprin, name='inicioprin'),
    path('selecuser', views.selecuser, name='selecuser'),
    path('contacto/', views.contacto, name= 'contacto'),
    path('categoria', views.categoria, name= 'categoria'),
    path('catkitchen', views.catkitchen, name= 'catkitchen'),
    path('catliving', views.catliving, name= 'catliving'),
    path('catbedroom', views.catbedroom, name= 'catbedroom'),
    path('catbathroom', views.catbathroom, name= 'catbathroom'),
    path('register', views.register, name='Register'),
    #path('registrarse/', views.registrarse, name= 'registrarse'),
    path('login/', views.login_request, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', LoginView.as_view(template_name='AppCliente/login.html'), name='Login'),
    path('editarperfil', views.editarperfil, name='Editarperfil'),
 
    
   
]

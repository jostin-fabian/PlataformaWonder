from django.urls import path

from wonder import views
from django.contrib.auth.views import *

urlpatterns = [

    # HOME
    path('home/', views.home, name='home'),

    # EntornoVirtual
    path('entornoVirtual/', views.entornoVirtual, name='entornoVirtual'),

    # EntornoVirtual
    path('entornoVirtual/<str:username>', views.entornoVirtualChat, name='entornoVirtualChat'),
    path('<int:reserva_id>/update_reserva/', views.update_reserva, name='update_reserva'),
    path('<int:reserva_id>/remove_question/', views.remove_reserva, name='remove_question'),
    # Contactanos
    path('contactanos/', views.contactanos, name='contactanos'),

    # Registro de Ususario
    path('registro/', views.registro, name='registro'),

    # Proyectos
    path('proyectos/', views.proyectos, name='proyectos'),

    path('login/', LoginView.as_view(template_name='wonder/Utils/wonderTemplate_HTML.html'), name="login")

]

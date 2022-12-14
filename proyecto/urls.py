"""proyecto URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from django.views.generic import TemplateView
from ejemplo.views import (index, saludar_a, buscar, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
from astros.views import (index, PostDetalle, PostListar, PostCrear, PostBorrar, PostActualizar, UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle, About)
=======
from ejemplo.views import (index, saludar_a, buscar, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
from ejemplo_dos.views import (index, PostDetalle, PostListar, PostCrear, PostBorrar, PostActualizar, UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle)
>>>>>>> cacbdb78ad7cd92d33e128e988329e7b3add8e17
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar-a/<nombre>/<apellido>/', saludar_a),
    path('buscar/', buscar),
    #path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
<<<<<<< HEAD
    path('astros/', index, name="astros-index"),
    path('astros/<int:pk>/detalle/', PostDetalle.as_view(), name="astros-detalle"),
    path('astros/listar/', PostListar.as_view(), name="astros-listar"),
    path('astros/crear/', staff_member_required(PostCrear.as_view()), name="astros-crear"),
    path('astros/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="astros-borrar"),
    path('astros/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="astros-actualizar"),
    path('astros/signup/', UserSignUp.as_view(), name ="astros-signup"),
    path('astros/login/', UserLogin.as_view(), name= "astros-login"),
    path('astros/logout/', UserLogout.as_view(), name="astros-logout"),
    path('astros/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="astros-avatars-actualizar"),
    path('astros/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="astros-users-actualizar"),
    path('astros/mensajes/crear/', MensajeCrear.as_view(), name="astros-mensajes-crear"),
    path('astros/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="astros-mensajes-detalle"),
    path('astros/mensajes/listar/', MensajeListar.as_view(), name="astros-mensajes-listar"),
    path('astros/about', TemplateView.as_view(template_name='astros/about.html'), name="astros-about"),
=======
    path('ejemplo-dos/', index, name="ejemplo-dos-index"),
    path('ejemplo-dos/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    path('ejemplo-dos/listar/', PostListar.as_view(), name="ejemplo-dos-listar"),
    path('ejemplo-dos/crear/', staff_member_required(PostCrear.as_view()), name="ejemplo-dos-crear"),
    path('ejemplo-dos/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="ejemplo-dos-borrar"),
    path('ejemplo-dos/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="ejemplo-dos-actualizar"),
    path('ejemplo-dos/signup/', UserSignUp.as_view(), name ="ejemplo-dos-signup"),
    path('ejemplo-dos/login/', UserLogin.as_view(), name= "ejemplo-dos-login"),
    path('ejemplo-dos/logout/', UserLogout.as_view(), name="ejemplo-dos-logout"),
    path('ejemplo-dos/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="ejemplo-dos-avatars-actualizar"),
    path('ejemplo-dos/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="ejemplo-dos-users-actualizar"),
    path('ejemplo-dos/mensajes/crear/', MensajeCrear.as_view(), name="ejemplo-dos-mensajes-crear"),
    path('ejemplo-dos/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="ejemplo-dos-mensajes-detalle"),
    path('ejemplo-dos/mensajes/listar/', MensajeListar.as_view(), name="ejemplo-dos-mensajes-listar"),

>>>>>>> cacbdb78ad7cd92d33e128e988329e7b3add8e17

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
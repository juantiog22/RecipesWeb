# recetas/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from .import views



urlpatterns = [
    path('', views.index, name='index'),
    path('busqueda', views.busqueda, name='busqueda'),
    path('busqueda/receta/<int:receta_id>/', views.receta, name='receta'),
    path('busqueda/editar/<int:receta_id>', views.editar, name='editar'),
    path('busqueda/create/', views.create, name='create'),
    path('eliminar/<int:receta_id>/', views.eliminarReceta, name='eliminar'),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
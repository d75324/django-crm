from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),

    # Cambio de contraseñas en 4 pasos.
    # Paso 1: Solicitud de email (Formulario para ingresar email)
    # urls.py
# ASUMIENTO que el nombre de tu aplicación es 'accounts' o similar

     path('password_reset/', 
          auth_views.PasswordResetView.as_view(
               template_name='registration/password_reset_form.html', # este es el template del formulario
               
               # definimos y direccionamos esta variable: html_email_template_name
               html_email_template_name='registration/password_reset_email.html',
               
               # texto plano de respaldo por si las moscas
               email_template_name='registration/pass_reset_email.txt', 
               
               subject_template_name='registration/password_reset_subject.txt'
          ), 
          name='password_reset'),

    # Paso 2: Email enviado (Página de confirmación después de enviar el email)
    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    # Paso 3: Confirmación de token (Formulario para ingresar la nueva contraseña)
    # Los argumentos uidb64 (user ID base64) y token son obligatorios aquí
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),

    # Paso 4: Contraseña cambiada (Página de confirmación final)
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(), 
         name='password_reset_complete'),
]
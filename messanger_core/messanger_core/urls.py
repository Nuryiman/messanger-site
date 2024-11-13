"""
URL configuration for messanger_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from users.views import (LoginView, RegisterView, MakeRegisterView, EditProfileView,
                         MakeLoginView, HomeView, MakeLogoutView, ProfileView, MakeEditProfileView, ChatView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home-url'),
    path('login/', LoginView.as_view(), name='login-url'),
    path('make-login/', MakeLoginView.as_view(), name='make-login-url'),
    path('register/', RegisterView.as_view(), name='register-url'),
    path('make-register/', MakeRegisterView.as_view(), name='make-register-url'),
    path('make-logout/', MakeLogoutView.as_view(), name='make-logout-url'),
    path('profile/', ProfileView.as_view(), name='profile-url'),
    path('edit-profile/', EditProfileView.as_view(), name='edit-profile-url'),
    path('make-edit-profile/', MakeEditProfileView.as_view(), name='make-edit-profile-url'),
    path('chat/', ChatView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

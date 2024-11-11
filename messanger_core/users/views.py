from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


class RegisterView(TemplateView):
    template_name = 'register.html'


class MakeRegisterView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        # print(request.COOKIES)
        name = data['name']
        phone = data['phone']

        try:
            CustomUser.objects.get(phone_number=phone)
            error = 'Пользователь с таким номером уже зарегистрирован'
            context = {
                'error': error
            }
            return render(request, 'register.html', context)

        except CustomUser.DoesNotExist:
            password1 = data['password1']
            password2 = data['password2']

            if password1 == password2:
                user = CustomUser.objects.create_user(first_name=name, phone_number=phone, password=password1)
                login(request, user)
                return redirect('home-url')
            else:
                error = 'Пароли не совпадают'
                context = {
                    'error': error
                }
                return render(request, 'register.html', context)


class LoginView(TemplateView):
    template_name = 'login.html'


class MakeLoginView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        phone = data['phone']

        try:
            user = CustomUser.objects.get(phone_number=phone)
        except CustomUser.DoesNotExist:
            error = 'Такой номер еще не зарегистрирован'
            context = {
                'error': error
            }
            return render(request, 'login.html', context)

        password = data['password']

        correct = user.check_password(password)
        if correct:
            login(request, user)
            return redirect('home-url')
        else:
            error = 'Неправильный пароль'
            context = {
                'error': error
            }
            return render(request, 'login.html', context)


class MakeLogoutView(View):

    def post(self, request, *args, **kwargs):

        logout(request)

        return redirect('login-url')


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            context = {
                'user': user
            }
            return render(request, 'index.html', context)
        else:
            return redirect('login-url')

    # def get_context_data(self, **kwargs):
    #     user = self.request.user


class ProfileView(TemplateView):
    template_name = 'profile.html'

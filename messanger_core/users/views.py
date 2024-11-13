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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем текущего пользователя и передаем в контекст
        user = self.request.user
        context['user'] = user

        # Поиск пользователей по запросу
        input_query = self.request.GET.get("search", "")
        print(input_query)

        if input_query:
            # Используйте кастомный метод поиска, если он есть
            search_users = CustomUser.objects.search(name=input_query)
        else:
            # Если ничего не введено в поиск, возвращаем всех пользователей
            search_users = CustomUser.objects.all()

        print(search_users)
        context['search_users'] = search_users
        context['input_query'] = input_query

        return context

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('login-url')

        return super().get(request, *args, **kwargs)




class ProfileView(TemplateView):
    template_name = 'profile.html'


class EditProfileView(TemplateView):
    template_name = 'edit_profile.html'


class MakeEditProfileView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        user = request.user

        name = data['name']
        phone = data['phone']
        birth_day = data['birth_day']
        bio = data['bio']

        user.first_name = name
        user.phone_number = phone
        if birth_day:
            user.birth_day = birth_day
        user.bio = bio
        user.save()
        return redirect('profile-url')


class ChatView(TemplateView):
    template_name = 'chat.html'
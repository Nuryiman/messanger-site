from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .forms import ProfileImage

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
        if not user.is_authenticated:
            return redirect('login-url')

        super().get(request, *args, **kwargs)
        input_query = request.GET.get("search", "")
        if input_query:
            search_users = CustomUser.objects.search(name=input_query)
        else:
            search_users = CustomUser.objects.all()

        context = {

            'user': user,
            'search_users': search_users,
            'input_query': input_query

        }
        return render(request, self.template_name, context)




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
            birth_day = data.get('birth_day')
            bio = data['bio']
            avatar = request.FILES.get('profile_image')  # Получаем загружаемое изображение

            user.first_name = name
            user.phone_number = phone
            if birth_day:
                user.birth_day = birth_day
            user.bio = bio
            if avatar:
                user.avatar = avatar  # Сохраняем изображение
            user.save()
            return redirect('profile-url')


class ChatView(TemplateView):
    template_name = 'chat.html'
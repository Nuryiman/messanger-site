from django.contrib.auth import login, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .forms import ProfileImage

from users.models import CustomUser, Chat, UserMessage


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

    def get(self, request, *args, **kwargs):

        logout(request)

        return redirect('login-url')


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('login-url')

        input_query = request.GET.get("search", "")
        if input_query:
            users = CustomUser.objects.search(name=input_query).exclude(id=user.id)
        else:
            users = Chat.objects.filter(Q(user1=user) | Q(user2=user)).exclude(id=user.id)

        context = {

            'user': user,
            'users': users,
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


class ChatView(View):
    template_name = 'chat.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user

        chats = Chat.objects.filter(Q(user1=user) | Q(user2=user))
        chat = Chat.objects.get(id=kwargs['pk'])
        if chat.user1 == user:
            companion = chat.user2
        else:
            companion = chat.user1

        chat_messages = UserMessage.objects.filter(Q(sender=user, receiver=companion) |
                                               Q(receiver=user, sender=companion)).order_by('created_at')

        context = {
            'chat': chat,
            'user': user,
            'companion': companion,
            'chats': chats,
            'chat_messages': chat_messages,
        }
        return render(request, self.template_name, context)


class SendMessageView(View):
    def post(self, request, *args, **kwargs):
        user = request.user

        companion = CustomUser.objects.get(id=kwargs['pk'])
        try:
            chat = Chat.objects.get(user1=user, user2=companion)
        except Chat.DoesNotExist:
            try:
                chat = Chat.objects.get(user2=user, user1=companion)
            except Chat.DoesNotExist:
                chat = Chat.objects.create(user1=user, user2=companion)

        message = request.POST['message']
        UserMessage.objects.create(
            sender=user,
            receiver=companion,
            text=message,
            chat=chat
        )
        return redirect('chat-url', pk=chat.id)

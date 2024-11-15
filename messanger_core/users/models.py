from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """Моделька для пользователей"""

    username = None
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    phone_number = models.CharField(
        max_length=25,
        validators=[MinLengthValidator(7)],
        unique=True)

    birth_day = models.DateField(
        null=True,
        blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)

    bio = models.CharField(max_length=200, null=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Chat(models.Model):
    """Моделька для чатов"""

    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user1_chats', null=True)
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user2_chats', null=True)

    class Meta:
        unique_together = ('user1', 'user2')


class UserMessage(models.Model):
    """Моделька для сообщений пользователей"""

    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver_messages')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages', null=True)

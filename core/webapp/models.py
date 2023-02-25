from django.db import models
from django.db.models import TextChoices


class Choice(TextChoices):
    ACTIVE = 'Active', 'Активна'
    BLOCKED = 'Blocked', 'Заблокировано'


class GuessBook(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False, verbose_name='Имя')
    email = models.EmailField(max_length=120, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время редактирования')
    status = models.CharField(choices=Choice.choices, default=Choice.ACTIVE, max_length=50, verbose_name='Статус')

    def __str__(self):
        return f'{self.name}'

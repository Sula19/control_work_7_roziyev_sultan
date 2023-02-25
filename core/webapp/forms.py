from django import forms
from django.core.exceptions import ValidationError
from webapp.models import GuessBook


class BookForms(forms.ModelForm):
    class Meta:
        model = GuessBook
        fields = ('name', 'email', 'text')
        labels = {
            'name': 'Имя автора',
            'email': 'Email автора',
            'text': 'Текст',
            'created_at': 'Дата и время создания',
            'updated_at': 'Дата и время редактирования',
            'status': 'Статус'
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Поле name должен иметь не менее 3 символов')
        return name

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 6:
            raise ValidationError('Поле text должен иметь не менее 3 символов')
        return text

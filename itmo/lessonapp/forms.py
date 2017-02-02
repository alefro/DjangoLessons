from django import forms
from .models import Student, Lesson


class AttendanceForm(forms.Form):
    """
    Форма, которая будет отображаться при отмечании студента на уроке.
    student - выпадающий список из студентов, которые находятся в таблице Student
    lesson - выпадающий список из студентов, которые находятся в таблице Lesson
    """
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    lesson = forms.ModelChoiceField(queryset=Lesson.objects.all())


class EnterForm(forms.Form):
    """
    Форма авторизации.
    login - обычный input
    password - инпут, к оторому подключен widget Password
    """
    login = forms.CharField(label='login', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class RegForm(forms.Form):
    """
    Форма регистрации пользователей.
    login, password, first_name, last_name, email - поля из класса User, стандартной аутентификации Django.
    """
    login = forms.CharField(label='login', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    email = forms.CharField(label='email', max_length=100)

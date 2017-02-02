import datetime
from django.db import models
from django.db.models import CharField, DateTimeField, TextField, \
    DateField, ForeignKey


class Student(models.Model):
    """
    Модель/таблица студентов.
    """
    name = CharField(max_length=100)
    created_at = DateTimeField()

    def __str__(self):
        """
        Переопределяем функцию для отображения - будем видеть имя студента.
        """
        return '{}'.format(self.name)


class Lesson(models.Model):
    """
    Модель/таблица занятий.
    """
    theme = CharField(max_length=100)
    description = TextField()
    date = DateField()

    def __str__(self):
        """
        Переопределяем функцию для отображения - будем видеть имя тему урока.
        """
        return '{}'.format(self.theme)


class Attendance(models.Model):
    """
    Модель/таблица, в которой будут отмечаться посещения.
    """
    student = ForeignKey(Student, on_delete=models.CASCADE) # Внешний ключ для связи с таблицей студентов
    lesson = ForeignKey(Lesson, on_delete=models.CASCADE) # Внешний ключ для связи с таблицей уроков
    created_at = DateTimeField(default=datetime.datetime.now) # Поле для хранения timestamp. По-умолчанию текущее время.

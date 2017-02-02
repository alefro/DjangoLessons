from django.contrib import admin
from .models import Lesson, Student, Attendance

admin.site.register(Lesson) # Подключаем нашу модель Lesson к админке
admin.site.register(Student) # Подключаем нашу модель Student к админке
admin.site.register(Attendance) # Подключаем нашу модель Attendance к админке

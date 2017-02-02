from django.shortcuts import render, get_object_or_404, \
    redirect
from .models import Lesson, Student, Attendance
from .forms import AttendanceForm, EnterForm, RegForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, 'lessonapp/index.html')


@login_required(login_url='/lessonapp/auth')
def students(request):
    _students = Student.objects.all()
    return render(request, 'lessonapp/students.html',  {'students': _students})


def lessons(request):
    _lessons = Lesson.objects.all()
    return render(request, 'lessonapp/lessons.html', {'lessons': _lessons})


def student(request, student_id):
    _student = Student.objects.get(pk=student_id)
    return render(request, 'lessonapp/student.html', {'student': _student})


def lesson(request, lesson_id):
    _lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessonapp/lesson.html', {'lesson': _lesson})


def attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        _student = request.POST.get('student')
        _lesson = request.POST.get('lesson')
        _attendance = Attendance(
            student=Student.objects.get(pk=_student),
            lesson=Lesson.objects.get(pk=_lesson)
        )
        _attendance.save()
        return redirect('lessonapp:student', student_id=_student)
    else:
        form = AttendanceForm()

    return render(request, 'lessonapp/attendance-form.html', {'form': form})


def auth_view(request):
    if request.method == 'POST':
        _login = request.POST.get('login')
        _password = request.POST.get('password')
        user = authenticate(username=_login, password=_password)
        if user:
            login(request, user)
            form = EnterForm(request.POST)
        else:
            form = EnterForm(request.POST)
    else:
        form = EnterForm()
    return render(request, 'lessonapp/auth-form.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/lessonapp/')


def reg_view(request):
    if request.method == 'POST':
        _login = request.POST.get('login')
        user = User.objects.create_user(username=_login)

        _password = request.POST.get('password')
        _first_name = request.POST.get('first_name')
        _last_name = request.POST.get('last_name')
        _email = request.POST.get('email')

        user.first_name = _first_name
        user.last_name = _last_name
        user.email = _email
        user.set_password(_password)

        user.save()
        form = RegForm(request.POST)
    else:
        form = RegForm()
    return render(request, 'lessonapp/reg-form.html', {'form': form})

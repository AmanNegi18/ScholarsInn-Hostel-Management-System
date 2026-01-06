from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, StudentExtraForm
from .models import Student, MessMenu, Notice

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='student_login')  # Redirects to login if not logged in
def home(request):
    return render(request, 'hostel front.html')  # This is your current home page template



def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check if the user is a student
            if hasattr(user, 'student'):  
                return redirect('home')  # student home page
            elif user.is_staff:
                return redirect('dashboard')  # admin dashboard
            else:
                messages.error(request, 'User does not have a proper role')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'student.html')



def parent_login(request):
    if request.method == 'POST':
        parent_id = request.POST.get('parent-id')
        student_id = request.POST.get('student-id')
        password = request.POST.get('password')
        # Add your parent authentication logic here
        messages.error(request, 'Invalid credentials')
    return render(request, 'parents login.html')


def parent_register(request):
    if request.method == 'POST':
        parent_name = request.POST.get('parent_name')
        parent_email = request.POST.get('parent_email')
        parent_phone = request.POST.get('parent_phone')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        student_id = request.POST.get('student_id')
        relation = request.POST.get('relation')
        
        if password != password2:
            messages.error(request, 'Passwords do not match')
        else:
            # Add your parent registration logic here
            # For now, just show success message
            messages.success(request, f'Parent account created for {parent_name}!')
            return redirect('parent_login')
    
    return render(request, 'parent-register.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid admin credentials')
    return render(request, 'admin login.html')


def register(request):
    if request.method == 'POST':
        u_form = RegisterForm(request.POST)
        s_form = StudentExtraForm(request.POST)
        if u_form.is_valid() and s_form.is_valid():
            user = u_form.save()
            student = s_form.save(commit=False)
            student.user = user
            student.save()
            messages.success(request, f'Account created for {user.username}!')
            return redirect('student_login')
    else:
        u_form = RegisterForm()
        s_form = StudentExtraForm()
    return render(request, 'register.html',
                  {'u_form': u_form, 's_form': s_form})



def dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None
    return render(request, 'admin-dashboard.html', {'student': student})


@login_required
def room_booking(request):
    return render(request, 'booking.html')



def mess_menu(request):
    menu_items = MessMenu.objects.all().order_by('day')
    return render(request, 'mess menu.html', {'menu_items': menu_items})



def notice_board(request):
    notices = Notice.objects.all()
    return render(request, 'noticeboard.html', {'notices': notices})



def parent_view(request, roll):
    student = get_object_or_404(Student, roll=roll)
    return render(request, 'parentsdashboard.html', {'student': student})
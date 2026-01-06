from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register/parent/', views.parent_register, name='parent_register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('room-booking/', views.room_booking, name='room_booking'),
    path('mess-menu/', views.mess_menu, name='mess_menu'),
    path('notices/', views.notice_board, name='notice_board'),
    path('parent/<str:roll>/', views.parent_view, name='parent_view'),
    path('', views.student_login, name='student_login'),
    path('login/parent/', views.parent_login, name='parent_login'),
    path('login/admin/', views.admin_login, name='admin_login'),
]
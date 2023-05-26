from django.urls import path

from core import views

urlpatterns = [
    # College
    path('college-create/', views.college_create_view,  name='college-create'),
    path('college-update/<int:pk>/', views.college_update_view,  name='college-update'),
    path('college-get/<int:pk>/', views.college_get_view,  name='college-get'),
    path('college-delete/<int:pk>/', views.college_delete_view,  name='college-delete'),
    path('college-list/', views.college_list_view,  name='college-list'),

    #teacher
    path('teacher-create/', views.teacher_create_view,  name='teacher-create'),
    path('teacher-update/<int:pk>/', views.teacher_update_view,  name='teacher-update'),
    path('teacher-get/<int:pk>/', views.teacher_get_view,  name='teacher-get'),
    path('teacher-delete/<int:pk>/', views.teacher_delete_view,  name='teacher-delete'),
    path('teacher-list/', views.teacher_list_view,  name='teacher-list'),
]
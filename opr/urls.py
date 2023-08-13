from django.urls import path
from . import views

urlpatterns = [
     path("all-data/",views.all_data,name="all_data"),
     path("single-data/",views.single_data,name="single_data"),
     path("filter-data/",views.filter_data,name="filter_data"),
     path("add-data/",views.add_data,name="add_data"),
     path('get-add-data/',views.get_add_data,name="get_and_add_data"),
     path('about-us/',views.about_us,name='about_us'),
     path('study/',views.my_study,name='my_study_data'),
     path('signup/',views.signup,name='create_account'),
     
     path('remove-student',views.remove_student_data, name='remove_student_data'),
     
     
     path('student-all-data/',views.student_all_data , name="student_all_data"),
     
     path('delete-student/<int:id>/',views.delete_student , name="delete_student"),
     
     
     path('teacher-data/',views.teacher_data,name="teacher_data"),
     path('teacher-data-delete/<int:id>/',views.teacher_data_delete,name="teacher_data_delete"),
     path('teacher-data-show/<int:id>/',views.teacher_single_data , name="teacher_single_data")
]


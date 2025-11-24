from django.urls import path 
from . import views 
 
urlpatterns = [ 
     # Students
    path('add/', views.add_student, name='add_student'), 
    path('getAll/', views.get_all_students, name='get_all_students'), 
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('search/', views.search_students, name='search_students'),

     # Universities
    path('addUniversity/', views.add_university, name='add_university'),
    path('getUniversities/', views.get_all_universities, name='get_all_universities'),

] 
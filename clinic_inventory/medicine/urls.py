from django.urls import path
from . import views

urlpatterns = [

path('',views.dashboard,name="dashboard"),

path('medicines/',views.medicine_list,name="medicine_list"),

path('add/',views.add_medicine,name="add_medicine"),

path('edit/<int:id>/',views.edit_medicine,name="edit_medicine"),

path('delete/<int:id>/',views.delete_medicine,name="delete_medicine"),

path('details/<int:id>/',views.medicine_detail,name="medicine_detail"),
path('medicine_table/', views.medicine_table, name='medicine_table')




]
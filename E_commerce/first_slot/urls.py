from django.urls import path
from . import views

app_name = "first_slot"

urlpatterns = [
    path('', views.home_buld, name='home'),
    path('phone/', views.work_buld, name='work'),
    path('phone/<int:my_id>/', views.work_list, name='work_id'),
    path('add/', views.add_item, name='add_item'),
    path('update/<int:my_id>', views.update_item, name='update_item'),
    path('delete/<int:my_id>', views.delete_item, name='delete_item')
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_tasks, name='show_tasks'),
    path('create_task', views.create_task, name='create_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('edit_task/<int:task_id>', views.edit_task, name='edit_task'),
    path('change_list/<int:task_id>/<is_complete>', views.change_list, name='change_list'),
]

from django.urls import path, include

from Todo import views

urlpatterns = [
    path('', views.showIndex, name='home'),
    path('Add_Todo/', views.add_todo, name='add_todo'),
    path('Delete_Todo/', views.delete, name='delete'),
    path('Update_Todo/', views.update, name='update'),
]

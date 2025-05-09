from django.urls import path
from .views import TaskList,TaskDetails,TaskCreate,TaskUpdate,TaskDelete,LogIn,Register_now

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('log-in/',LogIn.as_view(),name='log-in'),
    path('log-out/',LogoutView.as_view(next_page='log-in'),name='log-out'),
    path('register/',Register_now.as_view(),name='register'),

    

    path('',TaskList.as_view(),name='tasks'),

    #CRUD operations

    path('task/<int:pk>',TaskDetails.as_view(),name='task'),
    path('create-task/',TaskCreate.as_view(),name='create-task'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    

]
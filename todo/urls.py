from django.urls import path

from .views import TodoListView, TodoHomeView,TodoCreate,TodoUpdate,TodoDelete



urlpatterns = [
    path('', TodoHomeView.as_view() , name='home'),
    path('todo/',TodoListView.as_view(), name= 'todo'),
    path('todo/new/',TodoCreate.as_view(), name = 'new'),
    path('todo/<int:pk>/update/', TodoUpdate.as_view(), name = 'update'),
    path('todo/<int:pk>/delete/', TodoDelete.as_view(), name= 'delete')
]
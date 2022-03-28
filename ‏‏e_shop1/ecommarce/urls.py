from django.urls import path
from . import views
urlpatterns=[
    path('users',views.getUsers,name='users'),
    path('user',views.addUser,name='user'),
    path('updateuser/<str:pk>',views.updateUser,name='updateuser'),
    path('deleteuser/<str:pk>',views.deleteUser),
    path('login',views.Login)

]
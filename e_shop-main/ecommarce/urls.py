from django.urls import path
from . import views
urlpatterns=[
    path('users',views.getUsers,name='users'),
    path('user',views.addUser,name='user'),
    path('updateuser/<str:pk>',views.updateUser,name='updateuser'),
    path('deleteuser/<str:pk>',views.deleteUser),
    path('resetpassword/<str:pk>',views.Resetpassword),
    path('login',views.Login),
    path('products',views.getProducts,name='products'),
    path('product/<str:pk>',views.getProduct),
    path('addproduct',views.addProducts),
    path('updateproduct/<str:pk>',views.updateProduct),
    path('deleteproduct/<str:pk>',views.deleteProduct)
]

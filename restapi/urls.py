from . import views
from django.urls import path
from .views import ListProduct,DetailProduct,ListRegister,DetailRegister
urlpatterns =[
    path('product',ListProduct.as_view()),
    path('product/<int:pk>/',DetailProduct.as_view()),
    path('register/',ListRegister.as_view()),
    path('register/<int:pk>',DetailRegister.as_view()),
                ]
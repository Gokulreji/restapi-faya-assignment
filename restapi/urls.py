from . import views
from django.urls import path
from .views import ListProduct,DetailProduct,ListRegister,DetialRegister
urlpatterns =[
    path('product',ListProduct.as_view()),
    path('product/<int:pk>/',DetailProduct.as_view()),
    path('register/',ListRegister.as_view()),
    path('register/<int:pk>',DetialRegister.as_view()),
                ]
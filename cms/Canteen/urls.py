
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home"),
    path('showitems/', views.showitems, name="showitems"),
    path('payment/', views.payment, name="payment"),
    path('successful/', views.successful, name="successful"),
]

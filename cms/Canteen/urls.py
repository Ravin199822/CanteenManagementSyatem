from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('option/', views.option, name="option"),
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home"),
    path('orderhistory/',views.orderhistory,name="orderhostory"),
    path('orderhistory/<str:identity>',views.cancleorder,name="cancleorder"),
    path('showitems/', views.showitems, name="showitems"),
    path('payment/', views.payment, name="payment"),
    path('verifyorder/', views.verifyorder, name="verifyorder"),
    path('successful/', views.successful, name="successful"),
]

from django.urls import path
from .import views
from .views import change_password

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('order/', views.order_page, name='order'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.Register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
      path('change-password/', change_password, name='change_password'),
    

]
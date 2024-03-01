from django.urls import path
from . import views
urlpatterns = [
   
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('developer-page',views.developer_page,name='developer_page'),
    path('developer-profile',views.developer_profile,name='developer_profile'),

]

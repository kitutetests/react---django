from django.urls import path
from . import views
urlpatterns = [
   
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
    path('developer-page',views.developer_page,name='developer_page'),
    path('developer-profile',views.developer_profile,name='developer_profile'),
    path('post_rentals',views.post_rentals,name='post_rentals'),
    path('sell_property',views.sell_property,name='sell_property'),
    path('view_property',views.view_properties,name='view_property'),
    path('search_rentals',views.search_rental,name='search_rentals'),

]

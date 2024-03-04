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
    path('property_details/<int:pk>',views.rentals_details,name='property_details'),
    path('search_rentals',views.search_rental,name='search_rentals'),

    path('buy_property',views.properties_on_sale,name='buy_property'),

    path('view_property_on_sale_details/<int:pk>',views.property_on_sale_details,     name='view_property_on_sale_details'),

    path('search_property',views.search_property,name='search_property'),
]

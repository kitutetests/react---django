from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('terms-and-conditions',views.terms_and_conditions,name='terms-and-conditions'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('developer-page',views.developer_page,name='developer_page'),
    path('developer-profile',views.developer_profile,name='developer_profile'),
    path('developer-profile-update',views.developer_profile_update,name='developer_profile-update'),

    path('pay_rental',views.pay_for_rental,name='pay_rental'),

    path('post_rentals',views.post_rentals,name='post_rentals'),
    path('developer_properties',views.developer_properties,name='developer_properties'),
    path('sell_property',views.sell_property,name='sell_property'),
    path('view_property',views.view_properties,name='view_property'),
    path('edit_rental/<int:pk>',views.edit_rental,name='edit_rental'),
    path('delete_rental/<int:pk>',views.delete_rental,name='delete_rental'),
    path('delete_property/<int:pk>',views.delete_property,name='delete_property'),
    path('edit_property/<int:pk>',views.edit_on_sale_property,name='edit_property'),
    path('property_details/<int:pk>',views.rentals_details,name='property_details'),
    path('search_rentals',views.search_rental,name='search_rentals'),
    path('buy_property',views.properties_on_sale,name='buy_property'),
    
    path('view_property_on_sale_details/<int:pk>',views.property_on_sale_details,                       name='view_property_on_sale_details'),

    path('search_property',views.search_property,name='search_property'),
    path('faqs',views.faq_view,name='faq'),
    path('send_email',views.email,name="send_email")
]

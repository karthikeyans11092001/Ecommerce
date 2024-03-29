from django.urls import path
from .views import register,login_user,home,logout_user,myCart,UpdateProfile,about,create_profile,add_Product,profile,place_order,orders_view,view_order_products
urlpatterns=[
    path('signup/',register,name='signup'),
    path('login/',login_user,name='login'),
    path('home/',home,name='home'),
    path('logout/',logout_user,name='logout'),
    path('about/',about,name='about'),
    path('my-cart/',orders_view,name='myCart'),
    path('my-cart/<int:id>',view_order_products,name='myCart'),
    path('add-product/',add_Product,name='addProduct'),
    path('',login_user,name='login'),
    path('profile/',profile,name='profile'),
    path('profile/edit-profile/<int:pk>',UpdateProfile,name='edit-profile'),
    path('profile/create-profile/',create_profile,name='create-profile'),
    path('place_order/', place_order, name='place_order'),
]
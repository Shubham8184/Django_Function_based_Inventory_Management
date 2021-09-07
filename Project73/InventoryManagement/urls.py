from django.urls import path
from .views import Deleteview, Homeview,Aboutview,Addproductview, Loginuserview, Logoutview, Registeruserview,Showproductview, Updateview



urlpatterns=[
    path('home/',Homeview,name='home'),
    path('about/',Aboutview,name='about'),
    path('add/',Addproductview,name='addproduct'),
    path('show/',Showproductview,name='showproduct'),
    path('update/<int:update>',Updateview,name='update'),
    path('delete/<int:delete>',Deleteview,name='delete'),
    path('login/',Loginuserview,name='login'),
    path('register/',Registeruserview,name='register'),
    path('logout/',Logoutview,name='logout'),
]
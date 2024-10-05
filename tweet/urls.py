from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name="home" ),
    path('signup/',views.signup,name="signup" ),
    path('login/', views.login_user, name='login'),  
    path('logout/', views.logout_user, name='logout'),
    path('settings/', views.settings, name='settings'),
    path('search/', views.search, name='search'),
    path('update_credentails/', views.update_credentails, name='update_credentails'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('user_profile/<int:id>/', views.user_profile, name='user_profile'),
]
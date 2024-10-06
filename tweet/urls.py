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
    path('create_tweet/', views.create_tweet, name='create_tweet'),
    path('edit_tweet/<int:id>/', views.edit_tweet, name='edit_tweet'),
    path('edit_tweet_page/<int:id>/', views.edit_tweet_page, name='edit_tweet_page'),
    path('delete_tweet/<int:id>/', views.delete_tweet, name='delete_tweet'),
  
]
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', views.login_view, name="login"),
    path('court1/', views.scoreboard_view, name="court1"),
    path('court2/', views.court2_view, name="court2"),
    path('logout/', views.logout_view, name='logout'),
    path('court_one/', views.court_one_view, name='court_one' ),
    path('court_two/', views.court_two_view, name='court_two' ),
    
    

]
from django.urls import path, include
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('', views.home, name = "home"),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name="login"),
    path('court1/', views.scoreboard_view, name="court1"),
    path('court2/', views.court2_view, name="court2"),
    path('court3/', views.court3_view, name="court3"),
    path('court4/', views.court4_view, name="court4"),
    path('court5/', views.court5_view, name="court5"),
    path('court6/', views.court6_view, name="court6"),
    path('court7/', views.court7_view, name="court7"),
    path('court8/', views.court8_view, name="court8"),
    path('court9/', views.court9_view, name="court9"),
    path('logout/', views.logout_view, name='logout'),
    path('court_one/', views.court_one_view, name='court_one' ),
    path('court_two/', views.court_two_view, name='court_two' ),
    path('court_three/', views.court_three_view, name='court_three' ),
    path('court_four/', views.court_four_view, name='court_four' ),
    path('court_five/', views.court_five_view, name='court_five' ),
    path('court_six/', views.court_six_view, name='court_six' ),
    path('court_seven/', views.court_seven_view, name='court_seven' ),
    path('court_eight/', views.court_eight_view, name='court_eight' ),
    path('court_nine/', views.court_nine_view, name='court_nine' ),
    path('get_players/', views.get_players, name='get_players'),
    
    

]

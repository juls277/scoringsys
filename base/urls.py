from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('get_players/', views.get_players, name='get_players'),
    path('court/<str:court_number>/', views.court_view, name="court"),
    path('scoreboard/<str:court_number>/', views.scoreboard_view, name='scoreboard'),
]



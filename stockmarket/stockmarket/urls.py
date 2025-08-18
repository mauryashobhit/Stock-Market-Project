from django.contrib import admin
from django.urls import path, include
from stocks import views
app_name="stocks"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path("news/",views.news,name="news"),
    path('api/nifty50/', views.nifty50_data, name='nifty50_data'),
    path('nifty-chart/', views.niftychart, name='niftychart'),
    path('screener/', views.screener, name='screener'),
    path('login/',views.login,name="login")]

    

    

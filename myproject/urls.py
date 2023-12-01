from django.contrib import admin
from django.urls import  path
from myproject import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.myhome,name="homepage"),
]
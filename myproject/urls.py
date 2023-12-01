from django.contrib import admin
from django.urls import include, path
from myproject import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage', views.myHome,name="homepage"),
]
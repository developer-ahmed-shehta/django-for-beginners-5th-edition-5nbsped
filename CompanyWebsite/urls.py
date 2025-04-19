from django.urls import path
from django.contrib import admin
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/',AboutPageView.as_view(), name='about'),
]
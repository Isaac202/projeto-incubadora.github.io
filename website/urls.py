from django.urls import path
from website.views import home,apoie

urlpatterns = [
    path('', home, name="home"),
    path("apoie/",apoie,name="apoie")
]
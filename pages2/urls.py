from  django.urls import path
from .views import HomePagesView, AboutPageView

urlpatterns = [
    path("", HomePagesView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
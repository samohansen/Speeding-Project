from django.urls import path
from .views import loginPageView, aboutPageView ## statsPageView

urlpatterns = [
    path("", loginPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    # path("stats/", statsPageView, name="stats")
]

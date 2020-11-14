from django.urls import path
from .views import loginPageView, aboutPageView, indexPageView ## statsPageView

urlpatterns = [
    path("about/", aboutPageView, name="about"),
    path("login/", loginPageView, name='login'),
    path("", indexPageView, name="index"),
    # path("stats/", statsPageView, name="stats")
]

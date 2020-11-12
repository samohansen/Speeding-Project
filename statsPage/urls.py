from django.urls import path
from .views import statsPageView

urlpatterns = [
    path("stats/", statsPageView, name="stats")
]

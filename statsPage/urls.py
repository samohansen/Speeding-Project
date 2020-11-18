from django.urls import path
from .views import statsPageView, enterDataPageView

urlpatterns = [
    path("enterdata/", enterDataPageView, name="enterData"),
    path("display/", statsPageView, name="display")
]

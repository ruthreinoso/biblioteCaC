from django.urls import path
from core import views
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    #path('contact/', ContactPageView.as_view(), name='contact'),
]

from django.urls import path
from .views import SingUp


urlpatterns = [
    path('signup/', SingUp.as_view(), name="signup")
]

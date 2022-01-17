from django.urls import path

from .views import AccountView

urlpatterns = [
    path('change/',AccountView.as_view()),
    path('',AccountView.as_view())
]

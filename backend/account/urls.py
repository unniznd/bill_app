from django.urls import path

from .views import AccountView

urlpatterns = [
    path('<str:u>/',AccountView.as_view()),
    path('<str:u>/<int:c>/',AccountView.as_view())
]

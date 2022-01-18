from django.urls import path

from .views import AccountView, AccountReportView

urlpatterns = [
    path('change/',AccountView.as_view()),
    path('',AccountView.as_view()),
    path('report/',AccountReportView.as_view())
]

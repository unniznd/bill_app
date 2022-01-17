
from django.contrib import admin
from django.urls import path, include
from .serializers import CustomAuthToken, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomAuthToken.as_view()),
    path('stock/',include('stock.urls')),
    path('account/',include('accounts.urls')),
    path('expense/',include('expense.urls')),
    path('logout/',Logout.as_view())
]

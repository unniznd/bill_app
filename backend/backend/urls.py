
from django.contrib import admin
from django.urls import path, include
from .serializers import CustomAuthToken, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomAuthToken.as_view()),
    path('stock/',include('stock.urls')),
    path('sale/',include('sales.urls')),
    path('account/',include('account.urls')),
    path('logout/',Logout.as_view())
]

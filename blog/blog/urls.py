from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zal.urls')),
    path('',include('users.urls'))
]

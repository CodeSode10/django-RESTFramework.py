from django.contrib import admin
from django.urls import path, include
from Api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path('employee/', employees),

    path('employee/<int:pk>', employee),
]

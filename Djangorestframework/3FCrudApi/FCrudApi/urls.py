from django.contrib import admin
from django.urls import path
from Api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('empapi/', employeeApi),

]

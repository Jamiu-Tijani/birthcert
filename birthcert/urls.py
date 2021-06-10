"""birthcert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', user_create, name ='Reg'),
    path('login/', auth,name='Auth'),
    path('logout/', deauth, name = 'DeAuth'),
    path('', index , name = 'index'),
    path('tryReg/', try_reg, name = 'tryReg' ),
    path('tryAuth/', try_auth, name = 'tryAuth' ),
]

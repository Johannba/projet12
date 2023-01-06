"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from client.views import ClientViewset
from contract.views import ContractViewset
from event.views import EventViewset

from user.views import RegisterApi



client_router = routers.SimpleRouter()
client_router.register(r"client/?", ClientViewset, basename="client")

contract_router = routers.SimpleRouter()
contract_router.register(r"contract/?", ContractViewset, basename="contract")

contract_status_router = routers.SimpleRouter()
contract_status_router.register(r"contractstatus/?", ContractViewset, basename="contractstatus")

event_router = routers.SimpleRouter()
event_router.register(r"event/?", EventViewset, basename='event')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", RegisterApi.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path('api/', include(client_router.urls)),
    path('api/', include(contract_router.urls)),
    path('api/', include(contract_status_router.urls)),
     path('api/', include(event_router.urls)),
]

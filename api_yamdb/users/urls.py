from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (SignUp, UserViewSet, get_token)

router_v1 = DefaultRouter()

router_v1.register(
    r'users',
    UserViewSet,
    basename='users'
)

urlpatterns = [
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/auth/signup/', SignUp.as_view(), name='signup'),
    path('v1/', include(router_v1.urls)),
]

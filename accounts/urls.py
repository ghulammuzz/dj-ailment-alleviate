from django.urls import path

from .views import PeracikSignUpView, PeracikLoginView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('peracik/signup/', PeracikSignUpView.as_view(), name='peracik_signup'),
    path('peracik/login/', PeracikLoginView.as_view()), 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
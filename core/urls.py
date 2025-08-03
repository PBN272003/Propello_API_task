from django.urls import path
from .views import RegisterView, UserViewSet, FirmViewSet,register_page, login_page, dashboard_page
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Manually map the ViewSet methods
user_list = UserViewSet.as_view({
    'get': 'list',
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

firm_list = FirmViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

firm_detail = FirmViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='api-register'),
    # JWT Token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # User endpoints
    path('user/', user_list, name='user-list'),
    path('user/<int:pk>/', user_detail, name='user-detail'),

    # Firm endpoints
    path('firms/', firm_list, name='firm-list'),
    path('firms/<int:pk>/', firm_detail, name='firm-detail'),
    path('register/', register_page, name='register-page'),
    path('login/', login_page, name='login-page'),
    path('dashboard/', dashboard_page, name='dashboard-page'),  
]

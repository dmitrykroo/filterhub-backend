from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from .views import PostView, PostDetailsView, UserDetailsView

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('post/', PostDetailsView.as_view()),
    path('post/<int:pk>/', PostDetailsView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('account/', UserDetailsView.as_view()),
    path('accounts/', include('rest_registration.api.urls')),
]
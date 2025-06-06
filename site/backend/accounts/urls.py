from django.urls import path
from .views import LoginView, RegisterView, LogoutView, UserDetailView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
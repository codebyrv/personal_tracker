from django.urls import path
from accounts.views import*

urlpatterns = [
    
    path('dashboard/', HomeView.as_view(), name='dashboard'),

    path('register/', RegisterView.as_view(), name='register'),

    path('', UserLoginView.as_view(), name='login'),

    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('profile/', ProfileView.as_view(), name='profile'),

]
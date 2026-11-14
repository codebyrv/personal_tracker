from django.urls import path
from accounts.views import*

urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),

    path('register/', RegisterView.as_view(), name='register'),

    path('login/', UserLoginView.as_view(), name='login'),

    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('profile/', ProfileView.as_view(), name='profile'),

]
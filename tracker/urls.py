
from django.urls import path
from tracker.views import*

urlpatterns = [
    
path('dashboard/', HomeView.as_view(), name='dashboard'),    


]
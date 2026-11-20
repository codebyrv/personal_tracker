
from django.urls import path
from tracker.views import*

urlpatterns = [
    
path('dashboard/', HomeView.as_view(), name='dashboard'),
path('category/', CategoryView.as_view(), name='category'),
path('task/', TaskView.as_view(), name='task'),

]
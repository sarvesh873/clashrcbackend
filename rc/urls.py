from django.urls import path
from .views import login , signup


urlpatterns = [
    path('signup', signup, name='signup'),
    path('login',login, name='login'),
    
    # path('logout',logout, name='logout'),
    
    # path('result/',result),
    
    
]
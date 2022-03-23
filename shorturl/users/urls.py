from django.urls import path

from .views import user_register, user_login, user_logout, feedback

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('feedback/', feedback, name='feedback')
]
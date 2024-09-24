from django.urls import path
from UserManager.views.UserRegisterView import UserRegisterView
from UserManager.views.UserLoginView import UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='login'),

]

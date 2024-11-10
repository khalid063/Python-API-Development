from django.urls import path # type: ignore
from .views import get_user
from .views import (
    get_user,
    #RegistrationAPIView,
    register_user,			# have to import
    get_registrar_users_list,
    login_user,
)




urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('register/', register_user, name='register_user'),         # User Registration url
    path('register/user-list/', get_registrar_users_list, name='get_registrar_users_list'),
    path('login/', login_user, name='login_user'),
]





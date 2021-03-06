from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('logout/', views.UserLogout.as_view(), name='user_logout'),
    path('profile/<username>/', views.UserProfile.as_view(), name='user_profile'),
    path('edit_profile/', views.UserEditProfile.as_view(), name='user_edit_profile'),
    path("follow/", views.follow.as_view(), name="follow"),
    path("unfollow/", views.unfollow.as_view(), name="unfollow"),
    path("reset_password/", views.send_email.as_view(), name="reset_password"),
    path("confirm_password/<number>/<email>/", views.confirm_password.as_view(), name="confirm_password"),
    path("change_password/<email>/", views.change_password.as_view(), name="change_password"),
]

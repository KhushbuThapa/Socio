from django.urls import path
from . import views
from social_django.views import auth
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('all/', views.ProfileListView.as_view(), name='profile-list-view'),
    path('follow/', views.follow_unfollow_profile, name='follow-unfollow-view'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail-view'),
    path('public-profile/<str:username>/', views.public_profile, name='public-profile'),

    # Password Reset Urls
    # path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_email.html'), name='password_reset'),
    # path('password_reset_sent/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_email.html'), name='password_reset_confirm'),
    # path('reset_password_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),



]
from django.conf.urls import url
from .views import AdLoginView, SignupView, user_logout
from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
    )

app_name = 'account'

urlpatterns = [
    url(r'^login/$', AdLoginView.as_view(), name='login'),
    url(r'^logout/$', user_logout, name='user_logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('password_reset/', PasswordResetView.as_view(
        success_url=reverse_lazy('account:password_reset_done'),
        template_name='account/password_reset.html'
    ), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'
    ), name='password_reset_done'),
    path('password_reset/<str:uidb64>/<slug:token>', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('account:password_reset_complete')
    ), name='password_reset_confirm'),
    path('password_reset/complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

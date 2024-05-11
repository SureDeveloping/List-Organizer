from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, SignOutView


urlpatterns = [
    path('sign_in/', auth_views.LoginView.as_view(
        template_name = 'accounts/sign_in.html'
    ), name='sign_in'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),  
    path('sign_out/', SignOutView.as_view(), name='sign_out'),

]

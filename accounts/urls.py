from django.urls import path
from .views import SIGN_IN
from .views import SIGN_UP


urlpatterns = [
    path('sign_in/', SIGN_IN.as_view(), name='sign_in'),
    path('sign_up/', SIGN_UP.as_view(), name='sign_up')
]


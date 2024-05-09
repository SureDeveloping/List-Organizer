from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class SIGN_IN(TemplateView):
    template_name = 'accounts/sign_in.html'

class SIGN_UP(TemplateView):
    template_name = 'accounts/sign_up.html'


from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ListTemplateCreateView(TemplateView):
    template_name = 'lists/list_template.html'
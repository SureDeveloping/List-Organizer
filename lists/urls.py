from django.urls import path
from .views import ListTemplateCreateView

urlpatterns = [
    path('list_template/', ListTemplateCreateView.as_view(), name='list_template'),  
]

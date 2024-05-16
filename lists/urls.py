from django.urls import path
from .views import CreateListView, ListsOverview


urlpatterns = [
    path('create_list/', CreateListView.as_view(), name='create_list'),  
    path('overview_lists/', ListsOverview.as_view(), name='overview_lists'),
]

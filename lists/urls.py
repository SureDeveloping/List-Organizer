from django.urls import path
from .views import CreateListView, ListsOverview, UpdateListView



urlpatterns = [
    path('create_list/', CreateListView.as_view(), name='create_list'),  
    path('overview_lists/', ListsOverview.as_view(), name='overview_lists'),
    path('<int:pk>/update/', UpdateListView.as_view(), name='update_list'),
]

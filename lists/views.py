from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import ListTemplate
from django.views.generic import ListView
from .forms import ListCreateForm


# Create your views here.

class CreateListView(CreateView):
    model = ListTemplate
    form_class = ListCreateForm
    template_name = 'lists/create_list.html'
    success_url = reverse_lazy('create_list')

    def form_valid(self, form):
        form.instance.list_owner = self.request.user
        return super().form_valid(form)

class ListsOverview(ListView):
    model = ListTemplate
    template_name = 'lists/overview_lists.html'
    context_object_name = 'list_templates'
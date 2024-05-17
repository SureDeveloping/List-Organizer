from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
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

class UpdateListView(UpdateView):
    model = ListTemplate
    form_class = ListCreateForm
    template_name = 'lists/update_list.html' 
    
    def get_success_url(self):
        return reverse_lazy('overview_lists') 

    def post(self, request, *args, **kwargs):
        if "delete" in request.POST:
            self.object = self.get_object()
            self.object.delete()
            return redirect(self.get_success_url())
        else:
            return super().post(request, *args, **kwargs)
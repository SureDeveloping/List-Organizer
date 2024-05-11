from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


# Create your views here.

class SignUpView(View):
    form_class = SignUpForm
    template_name = 'accounts/sign_up.html'
    
    def get(self, request):
        form = self.form_class()

        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, message="User Created Successfully")
            return redirect(reverse('sign_in'))
        
        context = {'form': form}
        return render(request, self.template_name, context)


class SignOutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, message="You have been signed out")
        return HttpResponseRedirect(reverse('sign_in'))


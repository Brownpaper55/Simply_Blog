from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def logout_view(request):
    logout(request)
    return redirect('post_list')
    
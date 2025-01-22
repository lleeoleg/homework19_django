from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import User
from .forms import UserForm
from django.urls import reverse_lazy

# Create your views here.


class Create(CreateView):
    model = User
    template_name = 'index.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

class Detail(DetailView):
    model = User
    template_name = 'detail.html'
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
    
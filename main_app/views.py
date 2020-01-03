from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish


# Create your views here.
def home(request):
  wishes = Wish.objects.all()
  return render(request, 'home.html', {'wishes': wishes})

class AddWish(CreateView):
  model = Wish
  fields = '__all__'

class DeleteWish(DeleteView):
  model = Wish
  success_url = '/'
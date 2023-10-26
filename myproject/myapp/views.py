from django.shortcuts import render, redirect
from .forms import SampleModelForm

# Create your views here.

def create_view(request):
    if request.method == 'POST':
        form = SampleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SampleModelForm()
    return render(request, 'create.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def add_icecream(request):
    if request.method == 'POST':
        form = SampleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SampleModelForm()
    return render(request, 'ice.html', {'form': form})
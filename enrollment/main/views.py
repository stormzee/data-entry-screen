from django.shortcuts import render

from .forms import HospitalizationForm
# Create your views here.


def index(request):
    
    form = HospitalizationForm()
    if request.method == 'POST':
        form = HospitalizationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            
    ctx = {
        'form':form
    }
    
    
    return render(request, 'index.html', context=ctx)
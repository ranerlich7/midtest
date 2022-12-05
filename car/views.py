from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import Car, Employee, Treatment
# Create your views here.
from .forms import TreatmentForm

def cars(request):
    cars = Car.objects.all()
    return render(request,'cars.html', {'cars':cars})

def treatments(request):
    treatments = Treatment.objects.all()
    return render(request, 'treatments.html', {'treatments':treatments})

    
def treatment(request):
    form = TreatmentForm()
    # cars = Car.objects.all()
    # employees = Employee.objects.all()
    context = { 
            'form': form
            }
    if request.method == "GET":
        return render(request,"treatment.html",context=context)
    else:
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Saved Succesfuly!")
            redirect('cars')
    
        return render(request,"treatment.html",{'form':form})
        
def charts(request):
    t = Treatment.objects.all()[0]
    return render(request,"charts.html",{'t':t})
        
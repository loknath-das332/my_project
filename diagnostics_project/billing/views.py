from django.shortcuts import render, redirect
from .models import Patient, Test, Bill
from .forms import BillForm

def home(request):
    return render(request, 'billing/home.html')

def add_patient(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        phone = request.POST['phone']
        Patient.objects.create(name=name, age=age, phone=phone)
        return redirect('home')
    return render(request, 'billing/add_patient.html')

def generate_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            selected_tests = form.cleaned_data['tests']
            total_amount = sum(test.price for test in selected_tests)
            bill.total = total_amount
            bill.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = BillForm()
    return render(request, 'billing/generate_bill.html', {'form': form})

def all_bills(request):
    bills = Bill.objects.all()
    return render(request, 'billing/all_bills.html', {'bills': bills})


from django.shortcuts import get_object_or_404
from .forms import PatientForm

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, 'billing/add_patient.html', {'form': form})

def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('all_patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'billing/edit_patient.html', {'form': form})


def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('all_patients')
    return render(request, 'billing/delete_confirm.html', {'patient': patient})

def all_bills(request):
    bills = Bill.objects.all().order_by('-created_at')
    return render(request, 'billing/all_bills.html', {'bills': bills})


def all_patients(request):
    patients = Patient.objects.all().order_by('-created_at')
    return render(request, 'billing/all_patients.html', {'patients': patients})



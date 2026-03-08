from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from datetime import date,timedelta

def base(request):
    return render(request,'base.html')

def dashboard(request):

    total_medicines = Medicine.objects.count()

    low_stock = Medicine.objects.filter(stock__lt=10)

    near_expiry = Medicine.objects.filter(
        expiry_date__lte=date.today()+timedelta(days=30)
    )

    context = {
        'total_medicines':total_medicines,
        'low_stock':low_stock,
        'near_expiry':near_expiry
    }

    return render(request,'dashboard.html',context)


def medicine_list(request):

    search = request.GET.get('search')

    if search:
        medicines = Medicine.objects.filter(name__icontains=search)
    else:
        medicines = Medicine.objects.all()

    return render(request,'medicine_list.html',{'medicines':medicines})


def add_medicine(request):

    if request.method=="POST":

        Medicine.objects.create(
            name=request.POST['name'],
            code=request.POST['code'],
            category=request.POST['category'],
            manufacturer=request.POST['manufacturer'],
            expiry_date=request.POST['expiry'],
            price=request.POST['price'],
            stock=request.POST['stock'],
            description=request.POST['description']
        )

        return redirect('medicine_list')

    return render(request,'add_medicine.html')


def edit_medicine(request,id):

    medicine = get_object_or_404(Medicine,id=id)

    if request.method=="POST":

        medicine.price = request.POST['price']
        medicine.expiry_date = request.POST['expiry']
        medicine.category = request.POST['category']
        medicine.manufacturer = request.POST['manufacturer']
        medicine.stock = request.POST['stock']
        medicine.description = request.POST['description']

        medicine.save()

        return redirect('medicine_list')

    return render(request,'edit_medicine.html',{'medicine':medicine})


def delete_medicine(request,id):

    medicine = get_object_or_404(Medicine,id=id)
    medicine.delete()

    return redirect('medicine_list')


def medicine_detail(request,id):

    medicine = get_object_or_404(Medicine,id=id)

    return render(request,'medicine_detail.html',{'medicine':medicine})

def medicine_table(request):

    search = request.GET.get('search')

    if search:
        medicines = Medicine.objects.filter(name__icontains=search)
    else:
        medicines = Medicine.objects.all()

    return render(request,'medicine_table.html',{'medicines':medicines})
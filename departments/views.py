from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Product

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/department_list.html', {'departments': departments})

def department_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Department.objects.create(name=name, description=description)
        return redirect('department_list')
    return render(request, 'departments/department_form.html')

def department_update(request, pk):
    department = Department.objects.get(pk=pk)
    if request.method == 'POST':
        department.name = request.POST['name']
        department.description = request.POST['description']
        department.save()
        return redirect('department_list')
    return render(request, 'departments/department_form.html', {'department': department})

def department_delete(request, pk):
    department = Department.objects.get(pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'departments/department_confirm_delete.html', {'department': department})

def department_product_list(request):
    departments = Department.objects.prefetch_related('products').all()
    return render(request, 'departments/department_product_list.html', {'departments': departments})

def product_list(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    products = department.products.all()
    return render(request, 'departments/product_list.html', {'department': department, 'products': products})

def product_create(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Product.objects.create(name=name, description=description, price=price, department=department)
        return redirect('product_list', department_id=department.id)
    return render(request, 'departments/product_form.html', {'department': department})

def product_update(request, department_id, product_id):
    department = get_object_or_404(Department, id=department_id)
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect('product_list', department_id=department.id)
    return render(request, 'departments/product_form.html', {'department': department, 'product': product})

def product_delete(request, department_id, product_id):
    department = get_object_or_404(Department, id=department_id)
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list', department_id=department.id)
    return render(request, 'departments/product_confirm_delete.html', {'department': department, 'product': product})


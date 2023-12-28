from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def home_buld(request):
    return render(request, 'first_slot/main.html')

def work_buld(request):
    page_obj = item = Product.objects.all()

    item_name = request.GET.get('search')
    if item_name != '' and item_name is not None:
        page_obj = item.filter(name__icontains=item_name)

    paginator = Paginator(page_obj,2)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    libr = {"page_obj": page_obj}
    return render(request, 'first_slot/phone.html', libr)
 
def work_list(request, my_id):
    x = Product.objects.get(id=my_id)
    context = {
        'kiu': x
    }
    return render(request, 'first_slot/model.html', context)

@login_required
def add_item(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get("upload")
        seller = request.user
        item = Product(name=name,price=price,description=description, images=image,seller=seller)
        item.save()
        return redirect('first_slot:work')
    return render(request, 'first_slot/add_item.html')

def update_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == 'POST':
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload")
        item.save()
        return redirect('/phone/')
    libr = {'new_key': item}
    return render(request, 'first_slot/updateitem.html', libr)

def delete_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == 'POST':
        item.delete()
        return redirect('/phone/')
    libr = {'key': item}
    return render(request, 'first_slot/delete.html', libr)
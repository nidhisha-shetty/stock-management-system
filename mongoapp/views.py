from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Stock
from .forms import Stockf
# Create your views here.


# def home_view(request):
#     stud=Student.objects.all()
#     for x in stud:
#         print(x.name, x.age)
#     return HttpResponse("Hello wold")



def home_view(request):
    stock_data=Stock.objects.all()
    context={
        'stock_context':stock_data
    }
    return render(request, 'home.html', context)

def add_view(request):
    form=Stockf(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context={
        'context_form':form
    }
    return render(request, 'create.html', context)

def edit_view(request, pass_id):
	obj=Stock.objects.get(id=pass_id)
	form=Stockf(request.POST or None,  instance=obj)  #instance is used to dispaly data of each field from DB
	if form.is_valid():
		form.save()
		return redirect('/')
	context={
		"my_form": form,
		"object": obj
	}
	return render(request, "edit.html", context)

def delete_view(request, pass_id):
    obj=Stock.objects.get(id=pass_id)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context={
	    'object':obj
	}
    return render(request, "delete.html", context)

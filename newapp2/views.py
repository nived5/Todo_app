from django.shortcuts import render, redirect

from newapp2.form import ToDoForm
from newapp2.models import ToDo


# Create your views here.
def newstudy(request):
    return render(request,'test3.html')

def home(request):
    return render(request,'homepage.html')

def dashboard(request):
    return render(request,'indexdash1.html')



def create(request):
    form = ToDoForm()
    if request.method == 'POST' :
        data = ToDoForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('page4')
    return render(request,'create.html',{'form':form})


#read

def read(request):
    data = ToDo.objects.all()
    return render(request,'read.html',{'read':data})

def delt(request,id):
    data = ToDo.objects.get(id=id)
    data.delete()
    return redirect('read')
def update(request,id):
    Todo = ToDo.objects.get(id=id)
    form = ToDoForm (instance=Todo)
    if request.method =='POST':
        form = ToDoForm(request.POST,instance=ToDo)
        if form.is_valid():
            form.save()
            return redirect('page4')
    return render(request,'update.html',{'form':form})

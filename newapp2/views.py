from django.shortcuts import render

from newapp2.form import ToDoForm


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
    return render(request,'indexdash1.html',{'form':form})

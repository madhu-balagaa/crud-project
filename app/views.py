from django.shortcuts import redirect, render

from app.models import Student

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender') 
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
    return render(request,"index.html")


def updateData(request,id):
    d=Student.objects.get(id=id)
    context={"d":d}
    

    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect("/")




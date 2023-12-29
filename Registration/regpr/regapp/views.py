from django.shortcuts import render
from .forms import StudForm,SForm
from .models import stud

# Create your views here.

def show(request):
    return render(request,"home.html")

def register(request):
    title="Student Registration"
    form=StudForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data["s_name"]
        clas = form.cleaned_data["s_class"]
        addr = form.cleaned_data["s_addr"]
        school = form.cleaned_data["s_school"]
        email = form.cleaned_data["s_email"]
        
        p = stud(s_name=name,s_class=clas,s_addr=addr,s_school=school,s_email=email)
        p.save()
        return render(request,'ack.html',{"title":"Registered Successfully"})

    context={
        "title":title,
        "form":form
    }    
    return render(request,"register.html",context)

def existing(request):
    title="All Registered Students"
    queryset=stud.objects.all()

    context={
        "title":title,
        "queryset":queryset
    }
    return render(request,'existing.html',context)

def delete(request):
    title="Delete Student"
    form = SForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=stud.objects.filter(s_name=name).delete()
        return render(request,"ack.html",{'title':"Student Deleted Successfully"})
    context={
        'title':title,
        'form':form,
    }
    return render(request,'delete.html',context)
from django.shortcuts import render,HttpResponse,redirect
from app.forms import Employee,Student
from app.models import Students,Seller

# Create your views here.
def main(request):
    if request.method=='POST':
        form_with_data=Student(request.POST)
        if form_with_data.is_valid():
            name=form_with_data.cleaned_data['name']
            email=form_with_data.cleaned_data['email']
            phone_number=form_with_data.cleaned_data['phone_number']
            address=form_with_data.cleaned_data['address']
            course=form_with_data.cleaned_data['course']
            DOB=form_with_data.cleaned_data['DOB']
            marks=form_with_data.cleaned_data['marks']
            st=Students(name=name,email=email,phone_number=phone_number,address=address,course=course,DOB=DOB,marks=marks)
            st.save()
            return render(request,'submit.html',{'name':name})
        else:
            return render(request,'error.html',{'form':form_with_data})
    else:
        form=Student()
        context={
            'form':form
        }
            
        return render(request,'index.html',context)


def amazon(request):
    form=Seller()
    


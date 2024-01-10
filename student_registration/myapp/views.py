from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.



def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            mb = fm.cleaned_data['mobile']
            ad = fm.cleaned_data['address']
            sk = fm.cleaned_data['skill']
            gn = fm.cleaned_data['gender']
            reg = Student(name=nm,  mobile=mb, address=ad, skill=sk, gender=gn)
            reg.save()
            fm = StudentRegistration()
            
    else:
        fm = StudentRegistration() 
    stud = Student.objects.all()   
    return render(request, 'account/addandshow.html', {'form':fm, 'stud':stud})


def update_data(request, id):
    print(id)
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
           fm.save()
           
    else:
     pi = Student.objects.get(pk=id)
     fm = StudentRegistration(instance=pi)

    return render(request, 'account/update.html', {'form':fm})


# delete data from database
def delete_data(request, id):
 if request.method == 'POST':
    pi = Student.objects.get(pk=id) 
    pi.delete()
    return HttpResponseRedirect('/')
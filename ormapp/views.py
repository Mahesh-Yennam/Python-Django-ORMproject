from django.shortcuts import redirect, render
from .models import Account, Education, Education2, Emp, Project
from ormapp.forms import AccountForm, EducationForm, EducationForm2, EmpForm, ProjectFrom

def home(request):
    return render(request, 'home.html')

def add_emp(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')
    else:
        t='Employee Registration Form'
        f=EmpForm
        d={'title':t,
           'form':f}
        return render(request, 'form.html',d)

def list_emp(request):
    elist=Emp.objects.all()
    d={'el':elist}
    return render(request, 'elist.html',d)

def delete_emp(request,id):
    emp=Emp.objects.get(id=id)
    emp.delete()
    return redirect('/listemp')

def edit_emp(request,id):
    emp=Emp.objects.get(id=id)
    if request.method=='POST':
        f=EmpForm(request.POST, instance=emp)
        f.save()
        return redirect('/listemp')
    else:
        t='Employee Update Form'
        f=EmpForm(instance=emp)
        d={'title':t,
           'form':f}
        return render(request, 'form.html',d)

def delete_emp2(request):
    id=request.GET.get('id')
    emp=Emp.objects.get(id=id)
    emp.delete()
    return redirect('/listemp')

def add_acc(request):
    if request.method=='POST':
        f=AccountForm(request.POST)
        f.save()
        return redirect('/')
    else:
        t='Account Registration Form'
        f=AccountForm
        d={'title':t,
           'form':f}
        return render(request, 'form.html',d)

def list_acc(request):
    alist=Account.objects.all()
    d={'al':alist}
    return render(request, 'alist.html',d)

def delete_acc(request,id):
    acc=Account.objects.get(id=id)
    acc.delete()
    return redirect('/listacc')

def edit_acc(request,id):
    acc=Account.objects.get(id=id)
    if request.method=='POST':
        f=AccountForm(request.POST, instance=acc)
        f.save()
        return redirect('/listacc')
    else:
        t='Account Update Form'
        f=AccountForm(instance=acc)
        d={'title':t,
           'form':f}
        return render(request, 'form.html',d)

def add_edu(request):
    if request.method=='POST':
        f=EducationForm(request.POST)
        f.save()
        return redirect('/')
    else:
        t='Education Registration Form'
        f=EducationForm
        d={'title':t,
           'form':f}
        return render(request, 'form.html',d)

def list_edu(request):
    edulist=Education.objects.all()
    d={'edul':edulist}
    return render(request, 'edulist.html',d)

def delete_edu(request,id):
    edu=Education.objects.get(id=id)
    edu.delete()
    return redirect('/listedu')

def edit_edu(request,id):
    edu=Education.objects.get(id=id)
    if request.method=='POST':
        f=EducationForm(request.POST, instance=edu)
        f.save()
        return redirect('/listedu')
    else:
        t='Education Update Form'
        f=EducationForm(instance=edu)
        d={'title':t,
           'form':f}
        return render(request, 'form.html',d)

def add_edu2(request):
    if request.method=='POST':
        f=EducationForm2(request.POST)
        f.save()
        return redirect('/')
    else:
        t='Education Registration Form2'
        f=EducationForm2
        d={'title':t,
           'form':f}
        return render(request, 'form.html',d)

def list_edu2(request):
    edulist=Education2.objects.all()
    d={'edul':edulist}
    return render(request, 'edulist2.html',d)


def delete_edu2(request,id):
    edu=Education2.objects.get(id=id)
    edu.delete()
    return redirect('/listedu2')

def edit_edu2(request,id):
    edu=Education2.objects.get(id=id)
    if request.method=='POST':
        f=EducationForm2(request.POST, instance=edu)
        f.save()
        return redirect('/listedu2')
    else:
        t='Education Update Form2'
        f=EducationForm2(instance=edu)
        d={'title':t,
           'form':f}
        return render(request, 'form.html',d)

def add_pro(request):
    if request.method=='POST':
        f=ProjectFrom(request.POST)
        f.save()
        return redirect('/')
    else:
        t='Education Registration Form2'
        f=ProjectFrom
        d={'title':t,
           'form':f}
        return render(request, 'form.html',d)

def list_pro(request):
    pl=Project.objects.all()
    d={'pl':pl}
    return render(request, 'plist.html',d)

def edit_pro(request,id):
    pro=Project.objects.get(id=id)
    if request.method=='POST':
        f=ProjectFrom(request.POST, instance=pro)
        f.save()
        return redirect('/listpro')
    else:
        t='Project Update Form'
        f=ProjectFrom(instance=pro)
        d={'title':t,
           'form':f}
        return render(request, 'form.html',d)

def delete_pro(request,id):
    pro=Project.objects.get(id=id)
    pro.delete()
    return redirect('/listpro')
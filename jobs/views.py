from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from . models import Register,jobpro,jobseek,jobselection

# Create your views here.

def start(request):
    return render(request,'homepage.html')

def login(request):
    return render(request, 'loginpage.html')

@login_required
def signup(request):
    return render(request,'signuppage1.html')

def regsave(request):
    a = request.POST['username']
    b = request.POST['email']
    c = request.POST['phone']
    d = request.POST['password1']

    reg = Register(name=a, email=b, phone=c, password=d)
    isExists = reg.isExists()
    isExists1 = reg.isExists1()

    if isExists :
        messages.error(request, 'email already taken')
        return redirect('home2')

    elif isExists1 :
        messages.error(request, 'username already taken')
        return redirect('home2')
    else:
        messages.info(request, 'Account created successfully')
        reg.save()
        return redirect('home')


@login_required(login_url='home')
def loginauth(request):
    a=request.POST['username']
    reg = Register(name=a)
    m1=reg.m1()
    if not m1:
        messages.error(request,'username or password is incorrect')
        return redirect('home')

    m = Register.objects.get(name=a)

    if m.password != request.POST['password']:
        messages.error(request, 'username or password is incorrect')
        return redirect('home')
    else:
        request.session['member_id'] = m.id
        messages.info(request, 'login Successfully...')
        return redirect('first')

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return redirect('home1')
    #return render(request, 'loginpage.html')
    #return HttpResponse("You're logged out.")

@login_required(login_url='home')
def first(request):
    return render(request,'seekorpro.html')

def pro1(request):
    j = request.session['member_id']
    reg = jobpro.objects.all().filter(relation_id=j)
    return render(request,'pro1.html',{'RELATION':reg})

def pro2data(request):
    a = request.POST['place']
    b = request.POST['job']
    c = request.FILES['image']
    #d = request.POST['id']
    k = request.session['member_id']
    relation = jobpro(relation_id=k, location1=a, jobdes=b, jobimg=c)
    relation.save()

    j=request.session['member_id']
    reg = jobpro.objects.all().filter(relation_id=j)

    messages.info(request, 'job adding procedure successfully')
    return render(request,'pro1.html', {'RELATION':reg})

def jobdel(request):
    p = request.session['member_id']
    k=request.POST['id']
    print("member_id=",p)
    print("job_id=",k)
    jobpro.objects.filter(relation_id=p,id=k).delete()
    return redirect('pro2')

def seek1(request):
    return render(request,'seek1.html')

def seek2data(request):
    a1 = request.POST['place']
    p=request.session['member_id']
    relation2 = jobseek(relation2_id=p,location2=a1)
    relation2.save()
    #m1=jobseek.objects.filter(location2=a1)
    m2= jobpro.objects.filter(location1=a1)
    #j1 = request.session['member_id']
    if m2:
        j1 = request.session['member_id']
        reg = jobpro.objects.all().filter(location1=a1)
        messages.info(request, 'Here is the results....')
        return render(request, 'seek1.html', {'RELATION': reg})
    else:
        messages.info(request, 'Currently No jobs are available in this locality')
        return redirect('seek1')

def jobsel(request):
    k = request.session['member_id']
    p=request.POST['jobdes']
    relation3 = jobselection(relation3_id=k,jobdes=p)
    relation3.save()

    messages.info(request, 'Successfully applied this job ..Waiting for the call')
    return render(request, 'seek1.html')

def viewseekers(request):
    j = request.session['member_id']
    k = request.POST['jobdes']
    a = jobpro.objects.get(jobdes=k)
    b = jobselection.objects.filter(jobdes=k)
    print(a,b)
    if b:
        k1=jobselection.objects.filter(jobdes=k)
        print(k1)
        messages.info(request, 'Here is the results....')
        return render(request, 'final.html', {'RELATION': k1})
    else:
        messages.info(request, 'Nobody applied this type job')
        return redirect('pro2')

def features(request):
    return render(request,'features.html')

def pricing(request):
    return render(request,'pricing.html')
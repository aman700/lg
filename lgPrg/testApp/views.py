from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testApp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.

def h_v(request):
    return render(request,'testApp/home.html')
@login_required
def p1_v(request):
    return render(request,'testApp/p1.html')
@login_required
def p2_v(request):
    return render(request,'testApp/p2.html')

def lo_v(request):
    return render(request,'testApp/logout.html')

def rg_v(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testApp/rgform.html',{'form':form})

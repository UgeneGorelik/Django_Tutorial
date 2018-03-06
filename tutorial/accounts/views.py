from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import  UserCreationForm,PasswordChangeForm
from accounts.forms import RegistrationForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserChangeForm
from django.contrib.auth import  update_session_auth_hash
from django.contrib.auth.decorators import login_required


def home(request):
    numbers = [1,2,3,4,5]
    name='avi'
    args={
        'name':name,
         'numbers':numbers
    }
    return  render(request,'accounts/home.html',args)

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form =RegistrationForm()
        args={'form':form}
        return  render(request,'accounts/reg_form.html',args)


def profile(request):
    args ={'user':request.user}
    return  render(request,'accounts/profile.html',args)


def edit_profile(request):
    if request.method=='POST':
        form= EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
            form=EditProfileForm(instance=request.user)
            args={'form':form}
            return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method=='POST':
        form= PasswordChangeForm(data=request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
    else:
            form=PasswordChangeForm(user=request.user)
            args={'form':form}
            return render(request, 'accounts/change_password.html', args)



def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)
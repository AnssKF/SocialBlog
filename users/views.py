from django.shortcuts import render,redirect

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def register(request):
    if request.method == 'POST':
        regFrom = UserRegisterForm(request.POST)
        if regFrom.is_valid():
            regFrom.save()
            username = regFrom.cleaned_data.get('username')
            messages.success(request, f'Signed up succsessfully you can log in now')
            return redirect('login')
    else:
        regFrom = UserRegisterForm()
    return render(request,'users/register.html',{'regForm': regFrom})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request,'users/profile.html', { 'u_form':u_form, 'p_form':p_form })


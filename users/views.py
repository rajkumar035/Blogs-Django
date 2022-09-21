from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserNameForms, ProfileImageForms
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        UserEdit = UserNameForms(request.POST, instance=request.user)
        ProfileEdit = ProfileImageForms(request.POST, request.FILES, instance=request.user.profile)
        if UserEdit.is_valid() and ProfileEdit.is_valid():
            UserEdit.save()
            ProfileEdit.save()
            messages.success(request, f'Profile is Updated!')
            return redirect('profile')
    else:
        UserEdit = UserNameForms(instance=request.user)
        ProfileEdit = ProfileImageForms(instance=request.user.profile)
    
    context = {
        'UserEdit':UserEdit,
        'ProfileEdit': ProfileEdit
    }
    return render(request, 'users/profile.html', context)
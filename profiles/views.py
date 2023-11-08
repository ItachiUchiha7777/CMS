from django.shortcuts import render,redirect
from .models import UserProfile
from cmsapp.models import Post
from .forms import UpdateProfileForm
# Create your views here.
from django .contrib import messages

def profile(request, pk):
    # user_profile = UserProfile.objects.get(user=request.user)
    user_profile = UserProfile.objects.get(profile_id=pk)
    
    return render(request, 'profile.html', {'profile': user_profile})


def account(request):
    user_account=request.user.userprofile
    contex={"account": user_account}
    return render(request,"account.html",contex)

def UpdateProfile(request):
    profile=request.user.userprofile

    form=UpdateProfileForm(instance=profile)
    if request.method=="POST":
        form=UpdateProfileForm(request.POST,request.FILES,)
        if form.is_valid():
            form.save()
            messages.info(request,"You updated your profile")
            return redirect("account")
    contex={"form":form}
    return render(request, 'updateprofile.html',contex)
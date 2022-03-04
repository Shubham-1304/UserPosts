from django.shortcuts import render,redirect
from .models import User
from .forms import PostForm
from django.contrib import messages

def addPost(request):
    form=PostForm()
    if request.method=='POST':
        if request.user.is_authenticated:
            form=PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Posted successfully")
                return redirect('addPost')
        else:
            messages.error(request,"User not authenticated")
            print("User not authenticated")

    context={'form':form}
    return render(request,'addPost.html',context)
from django.shortcuts import render,redirect
from .models import User
from .forms import PostForm

def addPost(request):
    form=PostForm()
    if request.method=='POST':
        if request.user.is_authenticated:
            form=PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('addPost')
        else:
            print("User not authenticated")

    context={'form':form}
    return render(request,'addPost.html',context)
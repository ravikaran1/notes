from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as loginn,logout as logoutt
from django.contrib import messages
from .models import Note,querie
import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
def check(email):
    if(re.search(regex, email)):
        return 'valid'

    else:
        return 'invalid'


def index(request):
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        user=request.user

        if len(content)<1:
            messages.error(request,'Write some content, you fool.')
            return redirect('index')

        if user.is_authenticated:
            note=Note(title=title,content=content,user=user)
            note.save()
            messages.success(request,'Note added.')
            return redirect('notes')
        else:
            messages.error(request,'Please login first.')
            return redirect('login')

    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        lusername=request.POST['lusername']
        lpassword=request.POST['lpassword']
        user=authenticate(username=lusername,password=lpassword)

        if user is not None:
            loginn(request, user)
            messages.success(request,'Logged in successfully. (And Ravi is the best.)')
            return redirect('index')

        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    logoutt(request)
    messages.success(request,'Logged out successfully')
    return redirect('index')


def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        try:
            phone=int(email)
            p='yes'
        except:
            p='no'

        if p=='yes':
            if len(email)<10:
                messages.error(request,'Put valid email or phone number.')
                return redirect('signup')
        if p=='no':
            if check(email)=='invalid':
                messages.error(request,'Put valid email or phone number.')
                return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists.')
            return redirect('signup')
        if len(username)<4:
            messages.error(request,'Username is too short.')
            return redirect('signup')
        if len(pass1)<6:
            messages.error(request,'Password is too short.')
            return redirect('signup')
        if pass1!=pass2:
            messages.error(request,'Passwords do not match.')
            return redirect('signup')


        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=username
        myuser.save()
        messages.success(request,'Signed up successfully, please Log in.')
        return redirect('login')

    return render(request,'signup.html')

def notes(request):
    user=request.user
    if user.is_authenticated:
        user=request.user
        allnotes=Note.objects.filter(user=user).order_by('-timest')
        params={'allnotes':allnotes}
        return render(request,'notes.html',params
        )
    else:
        messages.error(request,'Please login first.')
        return redirect('login')

def viewnote(request,myid):
    note=Note.objects.filter(sno=myid)
    return render(request,'noteview.html',{'note':note[0]})

def delet(request,myid):
    note=Note.objects.filter(sno=myid)
    note.delete()
    return redirect('notes')

def queries(request):
    if request.method=='POST':
        email=request.POST.get('email')
        name=request.POST.get('name')
        issue=request.POST.get('issue')

        query=querie(email=email,name=name,issue=issue)
        query.save()
        messages.success(request,'Yes, you are. The query has been submitted.')
        return redirect('index')

    return render(request,'queries.html')

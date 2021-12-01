from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
    
def ChangePassword(r):
    if r.user.is_authenticated:
        if r.method == 'POST':
            try:
                Password = r.POST['Pword']
                u = User.objects.get(username=r.user.username)
                u.set_password(Password)
                u.save()
                messages.success(r,'Your Password is Changed Successfuly')
                return redirect('/Auth/Login')


            except:
                messages.error(r,'Something Went Wrong While Changing Your Password')
                return render(r,'Authentication/ChangePassword.html',{'Fb':'fixed-bottom'})

        else:
            return render(r,'Authentication/ChangePassword.html',{'Fb':'fixed-bottom'})

    else:
        messages.info(r,'First Login Please')
        return redirect('/Auth/Login')

def Profile(r):
    if r.user.is_authenticated:
        print(r.user.username)
        return render(r,'Authentication/Profile.html',{'Fb':'fixed-bottom'})

    else:
        messages.info(r,'First Login Please')
        return redirect('/Auth/Login')
def Login(r):
    if not r.user.is_authenticated:
        if r.method == 'POST':
            username = r.POST['Uname']
            password = r.POST['Pword']
            user = authenticate(r, username=username, password=password)
            if user is not None:
                login(r,user)
                messages.success(r,"You Have Logged In, Successfully")
                return redirect("/Auth/Profile")
            
            else:
                messages.error(r,"Please Check Your Username And Password, Again Carefully")
                return render(r,'Authentication/login.html',{'Fb':'fixed-bottom'})

        else:
            return render(r,'Authentication/login.html',{'Fb':'fixed-bottom'})

    else:
        messages.success(r,'You Have Already Loged In   ')
        return redirect('/Auth/Profile')
    

def signup(r):
    if r.method == 'POST':
        username = r.POST['Uname']
        if username == 'admin':
            messages.error(r,"Username can't be admin")
            return render(r,'Authentication/signup.html',{'Fb':'fixed-bottom'})

           
        else:
            First_name = r.POST['Fname']
            Last_name = r.POST['Lname']
            password1 = r.POST['password1']
            password2 = r.POST['password2']
            email = r.POST['Email']
            if len(username)>10:
                messages.warning(r,'Username Should Be Just')
                return render(r,'Authentication/signup.html')

            else:
                try:
                    u = User.objects.create_user(username, email, password1)
                    u.first_name = First_name
                    u.last_name = Last_name
                    u.save()
                    messages.success(r,'Successfuly, Created Your Account')
                    user = authenticate(r, username=username, password=password1)
                    login(r,user)
                    messages.success(r,"You Have Logged In, Successfully")
                    return redirect('/Auth/Profile')

                except Exception as e :
                        messages.error(r,'Something Is Wrong With The Information You Entered')
                        return render(r,'Authentication/signup.html')

    else:
        return render(r,'Authentication/signup.html')
    
def LogOut(r):
    logout(r)
    return render(r,'Authentication/Logout.html',{'Fb':'fixed-bottom'})

def ChangeInformation(r):
    messages.info(r,'This is Under Construction')
    return redirect('/Auth/Profile/')

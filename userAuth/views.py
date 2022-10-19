
from ast import Not
import cProfile
from email import message
from getpass import getuser
import imp
# import profile
from pyexpat.errors import messages
from tabnanny import check
from django import views
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from userAuth.models import Post
from .models import Post
# from .models import Profile

# Create your views here.


def signUp(request):

    # if request.method == "POST":
    #     username = request.POST.get("mobile")
    #     fname = request.POST.get('fname')
    #     lname = request.POST.get('lname')
    #     email = request.POST.get("email")
    #     mobile = request.POST.get("mobile")
    #     password = request.POST.get("pass")
    #     Cpassword = request.POST.get("cpass")

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobiles = request.POST['mobile']
        password = request.POST['pass']
        cPassword = request.POST['cpass']

        if len(mobiles) != 10:
            messages.error(request, 'message should be 10 digit')
            return redirect('home')
        elif password != cPassword:
            messages.error(request, 'Password Does not match.')
            return redirect('home')
        else:
            user = User.objects.create_user(
                username=mobiles, email=email, password=cPassword)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, 'Your account succesfully created')
            return redirect('login')

    dis = {'title': 'SignUp Form'}
    return render(request, 'signUp/index.html', dis)


def login(request):

    if request.method == 'POST':
        mobiles = request.POST['lmobile']
        cpassword = request.POST['lpass']

        user = authenticate(request, username=mobiles, password=cpassword)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login Succesfull')
            return redirect('mainApp')
        else:
            messages.error(request, 'Something went wrong')
            return redirect('login')

    dis = {'title': 'Social Media App'}
    return render(request, 'loginForm/index.html', dis)


def mainApp(request):
    if request.method == 'POST':
        userMessage = request.POST.get('userMessage')
        userImage = request.FILES.get('userImg')
        heading = request.POST.get('heading')
        user = request.user
        user = Post(caption=userMessage, image=userImage, user=user, heading=heading)
        user.save()
    allPost = Post.objects.all()
    datas = {'posts': allPost}
    return render(request, 'messPage/index.html', datas)


def logOut(request):
    auth_logout(request)
    return redirect('home')

def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('mainApp')


# def profile_view(request,username):
#     getUser = User.objects.filter(username=username)
#     if getUser :
#         profile = Profile.objects.get(user = getUser[0])
#         profile = Profile.objects.all()
#         data = {
#             'profile':profile,
#         }
#         return render(request,'messPage/userProfile.html',data)
#     else:
#         return redirect('mainApp')

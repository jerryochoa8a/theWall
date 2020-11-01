from django.shortcuts import render, redirect, HttpResponse
from wall_app.models import User, Message, Comment
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request, "login_page.html")

def reg(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')               #checks if there any errors if not then it will create a new user
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email'],
            password= pw_hash)
    return redirect('/')

def login(request):
    user = User.objects.filter(email= request.POST['login_email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['login_pw'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id  
            return redirect('/home')
    else:
        messages.error(request, "Wrong email or password")
    return redirect('/')

def home(request):
    if request.session['userid']:
        #messages.error(request, "Successfully registered (or logged in)!")
        return render(request, "home_page.html", 
        {"user": User.objects.get(id=request.session['userid']),
        "all_mess": Message.objects.all()})
    else:
        return redirect('/')

def post_mes(request):
    Message.objects.create(
        message=request.POST['message'],
        user_id=request.session['userid']
    )

    return redirect('/home')


def the_wall(request):
    if request.session['userid']:
        # messages.error(request, "Successfully registered (or logged in)!")
        return render(request, "the_wall.html", 
        {"user": User.objects.get(id=request.session['userid']),
        "all_mess": Message.objects.all()})
    else:
        return redirect('/')

def post_com(request, mess_id):
    Comment.objects.create(
        comment=request.POST['comment'],
        user_id=request.session['userid'],
        Message_id= mess_id
    )

    return redirect('/the_wall')















##################################################
def logout(request):
    request.session['userid'] = None 
    messages.error(request, "You have successfully logged out")
    return redirect('/') #i love alo
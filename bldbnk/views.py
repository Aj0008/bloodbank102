from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Donor
from django.contrib.auth.models import User, auth

# Create your views here.  

def display(request) :
     res =res = Donor.objects.all()
     name = User.username
     return render (request, 'results.html', {"res": res , "name" : name})



def red(request):

     return render (request, 'login.html')

def login(request) :
     if request.method == 'POST' :
          name = request.POST["name"]
          passwd = request.POST["pass"]
          user = auth.authenticate(username=name, password=passwd)
          if user is not None:
               auth.login(request, user)
               return redirect('display')
          else :
               messages.info(request,"Username Password MissMAtch")
               return redirect("/")
     else :
          return render (request, 'login.html')

def add(request) :
     if request.method == 'POST' :
          name = request.POST["name1"]
          dist = request.POST["dist"]
          cont1 = request.POST["cont"]
          grp = request.POST["grp"]
          
          if Donor.objects.filter(cont=cont1).exists():
                         messages.info(request, 'Donor With same Mail Exists')
                         return redirect('add')
          else :
               donor = Donor.objects.create(name=name, dist=dist, grp=grp, cont=cont1)
               donor.save();
               messages.info(request, 'New Donor Created')
               return redirect('display')
     else :

          return render(request, 'add.html')

def insert(request) :
     if request.method == 'POST' :

    #dnr4 = donor()
    #dnr4.id = 4
          name1 = request.POST["name1"]
          cont1 = request.POST["cont"]
          passwd1 = request.POST["passwd1"]
          passwd2 = request.POST["passwd2"]
          if passwd1 == passwd2 :
         
               if User.objects.filter(username=name1).exists():
                    messages.info(request, 'Username Taken')
                    return render(request, 'signup.html')
                    
               else :
                     if User.objects.filter(email=cont1).exists():
                         messages.info(request, 'User With same Mail Exists')
                         return render(request, 'signup.html')
                     else :
                         user = User.objects.create_user(username=name1, password=passwd1, email=cont1 )
                         user.save();
                         print ('user Created')
                   
          else :
               messages.info(request, 'Password Mismatch')
               return render(request, 'signup.html')
     else :
          return render(request, 'signup.html')
     res = User.objects.all()
    #res.append(dnr4)
    
     return render (request, 'login.html')



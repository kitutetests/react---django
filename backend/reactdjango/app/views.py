from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from . models import *
from django.contrib import auth,messages
from . forms import *
# Create your views here.
def register(request):
   
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']       

        if password1 == password2:
            user= User.objects.create_user(username=email,password=password1)
            user.save()

            profile=Profile(name=name,email=email)
            profile.save()

            return redirect(home)
        else:
                pass     

    else:
            pass    


    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
                
            auth.login(request, user)
        
            return redirect(developer_profile)
           
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    else:
        return render(request, 'login.html')

def home(request):
     return render(request, 'homepage.html')

def developer_page(request):
     user = request.user
     developer = Profile.objects.get(email=user.username)

     return render(request, 'developerpage.html',{'developer':developer})

def developer_profile(request):
     user = request.user
     developer = Profile.objects.get(email=user.username)
     return render(request, 'profile.html',{'developer':developer})

def post_rentals(request):
     user = request.user
     developer = Profile.objects.get(email=user.username)
     
     if request.method == 'POST':
          form = HouseRentForm(request.POST , request.FILES)

          if form.is_valid():
                post = form.save(commit=False)
                post.owner = developer
                post.save()
     else:
          form = HouseRentForm()
     return render (request , 'post-rentals.html',{'form':form})


def sell_property(request):
     user = request.user
     developer = Profile.objects.get(email=user.username)
     
     if request.method == 'POST':
          form = SellPropertyForm(request.POST , request.FILES)

          if form.is_valid():
                post = form.save(commit=False)
                post.owner = developer
                post.save()
     else:
          form = SellPropertyForm()
     return render (request , 'sellproperty.html',{'form':form})

def view_properties(request):
     rentals = Property_for_renting.objects.all()
     return render (request , 'rentals.html',{'rentals':rentals})
    
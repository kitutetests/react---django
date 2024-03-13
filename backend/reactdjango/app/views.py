from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from . models import *
from django.contrib import auth,messages
from . forms import ProfileForm,HouseRentForm,SellPropertyForm

from django.db.models import Q
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

# Create your views here.
def register(request):
   
    if request.method == 'POST':
        name = request.POST['name']
        other_name = request.POST['other_name']
        id_number = request.POST['id_number']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']       

        if password1 == password2:
            user= User.objects.create_user(username=email,password=password1,email=email)
            user.save()

            profile=Profile(user=user,name=name,other_name=other_name,id_number=id_number,email=email)
            profile.save()

            return redirect(login)
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
    
def logout(request):
    auth.logout(request)
    return redirect(login)

   
def home(request):
     return render(request, 'homepage.html')

def developer_page(request):
     user = request.user
     developer = Profile.objects.get(email=user.username)
     return render(request, 'developerpage.html',{'developer':developer})

def developer_profile(request):
     user = request.user
     developer = Profile.objects.get(email=user.username)

     return render(request, 'developer-profile.html',{'developer':developer})


def developer_profile_update(request):
     user = request.user
     developer = Profile.objects.get(email=user.username)
     
     if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            dp = form.cleaned_data['profile_picture']
            developer.profile_picture = dp
            developer.save()
            return redirect('developer_profile')  # Redirect to the developer profile page after saving
     else:
        form = ProfileForm() 

     return render(request, 'profile-update.html',{'form':form})



def post_rentals(request):
     user = request.user
     developer = Profile.objects.get(email=user.username)
     
     if request.method == 'POST':
          photos = request.FILES.getlist('photos')

          form = HouseRentForm(request.POST , request.FILES)
          
          if form.is_valid():
               post = form.save(commit=False)
               post.owner = developer
              
               post.save()

               photos = request.FILES.getlist('photos')

               for photo in photos:
                PropertyImage.objects.create(property_renting=post, image=photo)
               #  return render(post_rentals)
                
                
     else:
          form = HouseRentForm()
          
     return render (request , 'post-rentals.html',{'form':form,'developer':developer})

def developer_properties(request):
    user = request.user
    developer = Profile.objects.get(email=user.username)

    properties_for_renting = Property_for_renting.objects.filter(owner=developer)
    properties_on_sale = Property_on_sale.objects.filter(owner=developer)

    properties = list(properties_for_renting) + list(properties_on_sale)

    return render(request,'developer-property.html',{'properties':properties,'properties_for_renting':properties_for_renting,'properties_on_sale':properties_on_sale})

def edit_rental(request,pk):
    property_for_renting = Property_for_renting.objects.get(id=pk)

    if request.method == 'POST':
        apartment_name = request.POST['apartment_name']
        features = request.POST['features']
        price = request.POST['price']
        deposit = request.POST['deposit']
        water_fee = request.POST['water_fee']
        garbage_fee = request.POST['garbage_fee']
        contact = request.POST['contact']

        # assign new values
        property_for_renting.apartment_name = apartment_name 
        property_for_renting.features = features
        property_for_renting.price = price
        property_for_renting.deposit = deposit
        property_for_renting.water_fee = water_fee
        property_for_renting.garbage_fee = garbage_fee
        property_for_renting.contact = contact
        #save to db
        property_for_renting.save()
        return redirect(developer_properties)
    return render(request,'rental-edit.html',{'property_for_renting':property_for_renting})

def delete_rental(request,pk):
    property_for_renting = Property_for_renting.objects.get(id=pk)
    property_for_renting.delete()
    return redirect(developer_properties)

def edit_on_sale_property(request,pk):
    property_on_sale = Property_on_sale.objects.get(id=pk)
    if request.method == 'POST':
          features = request.POST['features']
          price = request.POST['price']
          deposit = request.POST['deposit']
          payment_process = request.POST['payment_process']
          contact = request.POST['contact']  
         
          property_on_sale.features = features
          property_on_sale.price = price
          property_on_sale.deposit = deposit
          property_on_sale.payment_process = payment_process
          property_on_sale.contact = contact

          property_on_sale.save()
          return redirect(developer_properties)
    return render(request,'on-sale-edit.html',{'property_on_sale':property_on_sale})

def delete_property(request,pk):
    property_on_sale = Property_on_sale.objects.get(id=pk)
    property_on_sale.delete()
    return redirect(developer_properties)


# post property for sale
def sell_property(request):
     user = request.user
     developer = Profile.objects.get(email=user.username)
     
     if request.method == 'POST':
          form = SellPropertyForm(request.POST , request.FILES)
          photos = request.FILES.getlist('photos')
          if form.is_valid():
                post = form.save(commit=False)
                post.owner = developer
                post.save()

                photos = request.FILES.getlist('photos')

                for photo in photos:
                    PropertyImage.objects.create(property_on_sale=post, image=photo)
     else:
          form = SellPropertyForm()
     return render (request , 'sellproperty.html',{'form':form,'developer':developer})

def view_properties(request):
     rentals = Property_for_renting.objects.all()
     paginator = Paginator(rentals, 4)
     page = request.GET.get('page')
     try:
          rentals = paginator.page(page)
   
     except PageNotAnInteger:
          # If page is not an integer, deliver first page.
          rentals = paginator.page(1)
     except EmptyPage:
          # If page is out of range (e.g. 9999), deliver last page of results.
          rentals = paginator.page(paginator.num_pages)

     return render (request , 'rentals.html',{'rentals':rentals})

def rentals_details(request, pk):
     rental = Property_for_renting.objects.get(id = pk)
     photos = rental.rental_photos.all()  # Assuming 'rental_photos' is the related name
     features_list = rental.features.split('.') if rental.features else []
     related_rentals = Property_for_renting.objects.filter(location = rental.location, size = rental.size).exclude(id=pk)
     return render (request , 'rentaldetails.html',{'rental':rental,'photos':photos,'features_list':features_list,'related_rentals':related_rentals})
     

def search_rental(request):
    query_location = request.POST['location']
    query_size = request.POST['Size']
    query_min_rent = request.POST['min-rent']
    query_max_rent = request.POST['max-rent']
    query_features = request.POST['Features']
    if request.method == 'POST':
         rentals = Property_for_renting.objects.all()
         if query_location:
            rentals = rentals.filter(location__icontains=query_location)
         if query_size:
            rentals = rentals.filter(size__icontains=query_size)
         if query_min_rent and query_max_rent:
            rentals = rentals.filter(price__range=(query_min_rent, query_max_rent))
         if query_features:
            rentals = rentals.filter(features__icontains=query_features)
        
    return render(request ,'searchrental.html',{'rentals':rentals})


def properties_on_sale(request):
     properties = Property_on_sale.objects.all()
     paginator = Paginator(properties, 4)
     page = request.GET.get('page')
     try:
          properties = paginator.page(page)
   
     except PageNotAnInteger:
          # If page is not an integer, deliver first page.
          properties = paginator.page(1)
     except EmptyPage:
          # If page is out of range (e.g. 9999), deliver last page of results.
          properties = paginator.page(paginator.num_pages)
     return render(request, 'buyproperty.html' ,{'properties':properties})


def property_on_sale_details(request, pk):
     on_sale_property = Property_on_sale.objects.get(id = pk)

     photos = on_sale_property.property_on_photos.all()

     features_list = on_sale_property.features.split('.') if on_sale_property.features else []

     related_property = Property_on_sale.objects.filter(

                         Q(location=on_sale_property.location, property_type=on_sale_property.property_type) | 
                         Q(property_type=on_sale_property.property_type, price=on_sale_property.price)
                         ).exclude(id=pk)                  

     return render (request , 'on_sale_property_details.html',{'on_sale_property':on_sale_property,'features_list':features_list,'related_property': related_property,'photos':photos})
  

def search_property(request):
    query_location = request.POST['location']
    query_min_price = request.POST['min-Price']
    query_max_price = request.POST['max-Price']
    query_type = request.POST['Size']

    if request.method == 'POST':
         properties = Property_on_sale.objects.all()
         if query_location:
            properties = properties.filter(location__icontains=query_location)

         if query_min_price and query_max_price:
            properties = properties.filter(price__range=(query_min_price, query_max_price))

         if query_type:
            properties = properties.filter(property_type__icontains=query_type)
        
    return render(request ,'search_property_on_sale.html',{'properties':properties})

def faq_view(request):
    return render(request, 'faq.html')

def email(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']

        
        send_mail(
            email,  # Subject
            message,  # Message
            email , # From email
            ['geffmutua001@gmail.com'],  # To email
            fail_silently=False,
                )
       
    return render(request,'email.html')   
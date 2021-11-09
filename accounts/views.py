from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from . models import Customer
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        pincode = request.POST['pincode']
        city = request.POST['city']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exist's")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "email already exist's")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save()
                customer_obj = Customer(user=user, mobile_number=mobile_number, city=city, pincode=pincode, address=address)
                customer_obj.save()
                messages.success(request, "Registered successfully")
                return redirect('login')
        else:
            messages.error(request, "password's doesn't match")
            return redirect('register')

    return render(request, 'accounts/register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, "invalid username or password")
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout_user(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    user = get_object_or_404(User, pk=request.user.id)
    customer = get_object_or_404(Customer, user=request.user)
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        city = request.POST['city']
        pincode = request.POST['pincode']
        mobile_number = request.POST['mobile_number']
        address = request.POST['address']

        user.first_name = firstname
        user.last_name = lastname
        customer.city = city
        customer.pincode = pincode
        customer.mobile_number = mobile_number
        customer.address = address

        user.save()
        customer.save()
        messages.success(request, "profile updated successfully")
        return redirect('profile')

    context = {
        'user' : user,
        'customer' : customer,
    }

    return render(request, 'accounts/profile.html', context)

from django.shortcuts import redirect, render
from . models import Slider, Team, Contact
from fooditems.models import Item

# Create your views here.
def home(request):
    sliders = Slider.objects.order_by('-created_date')
    featured_items = Item.objects.filter(is_available=True).filter(is_featured=True)[:5]
    latest_items = Item.objects.order_by('-last_modified').filter(is_available=True)[:10]
    context = {
        'sliders' : sliders,
        'featured_items' : featured_items,
        'latest_items' : latest_items,
    }
    return render(request, 'webpages/home.html', context)



def about(request):
    members = Team.objects.all()
    context = {
        'members' : members,
    }
    return render(request, 'webpages/about.html', context)
    

def contact(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        subject = request.POST['subject']
        details_message = request.POST['details_message']

        c = Contact(firstname=firstname, lastname=lastname, email=email, phone_number=phone_number, subject=subject, details_message=details_message)
        c.save()
        return redirect('home')

    return render(request, 'webpages/contact.html')

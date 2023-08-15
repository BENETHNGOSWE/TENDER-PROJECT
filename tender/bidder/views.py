from django.shortcuts import render,redirect
from .forms import Regform, applicationform
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import BidderReg,SelectedBidder
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404


# Create your views here.
def index_view(request):
    return render(request, 'select_role.html')



def vendorreg(request):
    if request.method =='POST':
       form =Regform(request.POST)
       if form.is_valid():
           form.save()
           return redirect('success_page')
    else:
        form=Regform()
    return render(request, 'vendorregform.html',{'form':form})


def vendorhome(request):
    return render(request, 'vendor.html')




def bid_application(request):
    if request.method == "POST":
        form = applicationform(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('bidder_dashboard')  

    else:
            form = applicationform()
            return render(request, "bid_applicationform.html", {"form":form}) 

def register_bidder(request):
    REGION_CHOICES = BidderReg.REGION_CHOICES
    DISTRICT_CHOICES = BidderReg.DISTRICT_CHOICES

    context = {
        'region_choices': REGION_CHOICES,
        'district_choices': DISTRICT_CHOICES,
    }

    if request.method == 'POST':
        # Process form submission here
        username = request.POST['username']
        password = request.POST['password']
        # Create a new user with only the username and password
        user = User.objects.create_user(username=username, password=password)
        # Get all other registration details from the form
        company_name = request.POST['company_name']
        tin_no = request.POST['tin_no']
        company_reg_no = request.POST['company_reg_no']
        vat_no = request.POST['vat_no']
        location = request.POST['location']
        region = request.POST['region']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        website = request.POST['website']
        business = request.POST['business']
        category = request.POST['category']
        foreign_input = request.POST['foreign_input']
        employee_num = request.POST['employee_num']
        passwords = request.POST['passwords']
        # Set all the details in the student model
        bidder = BidderReg.objects.create(
            user=user,
            companyName=company_name,
            tinNo=tin_no,
            companyRegNo=company_reg_no,
            vatNo=vat_no,
            location=location,
            region=region,
            district=district,
            phone=phone,
            email=email,
            website=website,
            business=business,
            category=category,
            foreignInput=foreign_input,
            employeeNum=employee_num,
            passwords=passwords
        )

        # Perform authentication and login
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login_bidder')

    return render(request, 'registration.html', context)


def upload_cv(request, biddereg_id):
    bidder = get_object_or_404(BidderReg, pk=biddereg_id)
    if request.method == 'POST':
        cv_file = request.FILES.get('cv')

        selected_bidder = SelectedBidder.objects.get(bidder=bidder)
        selected_bidder.cv = cv_file
        selected_bidder.save()

        return redirect('bidder_dashboard')  # Redirect the student to the dashboard after successful CV upload

    return render(request, 'upload_cv.html', {'bidder': bidder})
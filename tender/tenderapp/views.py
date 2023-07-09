from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Bidder, CVDocument,TenderReg
from django.contrib.auth.models import User
from bidder.models import bidapplication,BidderReg,SelectedBidder
from django.shortcuts import render,redirect,get_object_or_404
from .forms import TenderRegForm
# View for student registration
def register_bidder(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Create a new student user
        user = User.objects.create_user(username=username, password=password)
        # Create a corresponding Student model instance
        student = Bidder.objects.create(user=user)
        return redirect('login_bidder')
    return render(request, 'registration.html')

# View for student login
def login_bidder(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the student
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bidder_dashboard')
        else:
            # Invalid login credentials
            return render(request, 'loginpage_bidder.html', {'error': 'Invalid username or password.'})
    return render(request, 'loginpage_bidder.html')

def bidder_dashboard(request):
    job_positions = TenderReg.objects.all()
    return render(request, 'dashboard_bidder.html', {'job_positions': job_positions})


# @login_required
# def bidder_dashboard(request):
#     # Get all job positions
#     job_positions = TenderReg.objects.all()
#     return render(request, 'dashboard_bidder.html', {'job_positions': job_positions})

# View for CV document submission
@login_required
def submit_cv(request):
    if request.method == 'POST':
        cv_file = request.FILES['cv_file']
        # Save the CV document for the logged-in student
        CVDocument.objects.create(student=request.user.student, document=cv_file)
        return redirect('student_dashboard')
    return render(request, 'submit_cv.html')


def login_client(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the client
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('client_dashboard')
        else:
            # Invalid login credentials
            return render(request, 'loginpage.html', {'error': 'Invalid username or password.'})
    return render(request, 'loginpage.html')

# View for creating a job position
@login_required
def create_tender(request):
    if request.method == 'POST':
        title = request.POST['title']
        # Create a new job position for the logged-in client
        TenderReg.objects.create(title=title, client=request.user)
        return redirect('client_dashboard')
    return render(request, 'create_job_position.html')

# View for teacher dashboard
@login_required
def client_dashboard(request):
    # Get the job positions for the logged-in teacher
    job_positions = TenderReg.objects.filter(client=request.user)
    bid_applications = []
    for job_position in job_positions:
        applications = bidapplication.objects.filter(tender=job_position).order_by('price', 'time_to_complete')[:3]
        bid_applications.extend(applications)

    return render(request, 'dashboard_client.html', {'job_positions': job_positions, 'bid_applications': bid_applications})

@login_required
def best_students(request, job_position_id):
    job_position = TenderReg.objects.get(id=job_position_id)
    # Get the top three bid applications for the job position based on price and time to complete
    bid_applications = bidapplication.objects.filter(tender=job_position).order_by('price', 'time_to_complete')[:3]

    return render(request, 'best_students.html', {'job_position': job_position, 'bid_applications': bid_applications})







def tenderreg(request):
    if request.method == 'POST':
        form = TenderRegForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('alltenders')
    else:
        form = TenderRegForm()
    return render(request, 'tenderreg.html', {'form': form})

@login_required
def tenders_list(request):
    tenders = TenderReg.objects.filter(client=request.user)
    return render(request, 'alltenders.html', {'tenders': tenders})

# def tenders_list(request):
#     tenders = TenderReg.objects.all()
#     return render(request, 'alltenders.html', {'tenders': tenders})


@login_required
def student_dashboard(request):
    # Retrieve all available job positions
    job_positions = TenderReg.objects.all()
    return render(request, 'student_dashboard.html', {'job_positions': job_positions})


def tenders_list_bidder(request):
    tenders=TenderReg.objects.all()
    return render(request, 'alltenders_bidder.html',{'tenders':tenders})




def viewtender(request,pk):
    tender =TenderReg.objects.get(tenderid=pk)
    return render(request, 'viewtender.html',{'tender':tender})



def applytender(request):
    return render(request, 'application.html')


def select_candidates(request):
    if request.method == 'POST':
        tender_name = request.POST.get('tender_name')
        tender = get_object_or_404(TenderReg, tender_name=tender_name, client=request.user.client.user)  # Update the field name and filter by user instance
        bidders = bidapplication.objects.filter(tender=tender).order_by('price', 'time_to_complete')[:3]
        # Process the selected bidders here
        # You can perform actions such as updating their status or notifying them
        return render(request, 'bidder_selection.html', {'bidders': bidders, 'selected_tender': tender})
    else:
        tenders = TenderReg.objects.filter(client=request.user.client.user)  # Filter by user instance
        return render(request, 'test.html', {'tenders': tenders})

# def select_candidates(request):
#     if request.method == 'POST':
#         tender_name = request.POST.get('tender_name')
#         tender = get_object_or_404(TenderReg, tender_name=tender_name, teacher=request.user)  # Update the field name and filter by teacher
#         bidders = bidapplication.objects.filter(tender=tender).order_by('price', 'time_to_complete')[:3]
#         # Process the selected bidders here
#         # You can perform actions such as updating their status or notifying them
#         return render(request, 'bidder_selection.html', {'bidders': bidders, 'selected_tender': tender})
#     else:
#         tenders = TenderReg.objects.filter(teacher=request.user)  # Filter by teacher
#         return render(request, 'test.html', {'tenders': tenders})
    
    

def tender_details(request, tender_id):
    tender = TenderReg.objects.get(tenderid=tender_id)
    bidders = bidapplication.objects.filter(tender=tender).order_by('price', 'time_to_complete')
    return render(request, 'bidder_selection.html', {'bidders': bidders, 'selected_tender': tender})

def view_bidder(request, bidder_id):
    bidder = get_object_or_404(BidderReg, id=bidder_id)
    return render(request, 'details.html', {'bidder': bidder})


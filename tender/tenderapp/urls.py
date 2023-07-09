from django.urls import path
from . import views

urlpatterns = [
    path('register/bidder', views.register_bidder, name='register_bidder'),
    path('login/bidder', views.login_bidder, name='login_bidder'),
    path('submit-cv', views.submit_cv, name='submit_cv'),
    path('login/client', views.login_client, name='login_client'),
    path('create_tender', views.create_tender, name='create_tender'),
    path('bidder/dashboard', views.bidder_dashboard, name='bidder_dashboard'),
    path('client/dashboard', views.client_dashboard, name='client_dashboard'),
    path('best-students/<int:tenderreg_id>', views.best_students, name='best_students'),


    path('alltenders',views.tenders_list,name='alltenders'),
    path('alltendersbidder/',views.tenders_list_bidder,name='alltendersbidder'),
    path('tenderreg/',views.tenderreg,name='tenderreg'),
    path ('viewtender/<str:pk>/',views.viewtender, name='viewtender'),
    path ('application',views.applytender, name='application'),
#    path('tenders/<int:tender_id>/select-candidates/', select_candidates, name='select_candidates'),

    path('tenders/',views.select_candidates, name='select_candidates'),
    path('tender/<str:tender_id>/',views.tender_details, name='tender_details'),
    path('view_bidder/<int:bidder_id>/',views.view_bidder, name='view_bidder'),

]

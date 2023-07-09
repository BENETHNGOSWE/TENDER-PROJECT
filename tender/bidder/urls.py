from django.urls import path
from .views import upload_cv,register_bidder,bid_application,vendorreg, vendorhome,index_view

urlpatterns = [
    path('', index_view, name='index_view'),
    # path('', dashboard, name='dashboard'),
    path('vendorreg',vendorreg, name='vendorreg'),
    path('bidapplication', bid_application, name='bid_application'),
    path('vendor',vendorhome, name='vendor'),
    path('success_page', vendorhome, name='success_page'),
    path('bidder/',register_bidder, name='register_bidder'),
    # path('login/', login_client, name='login_client'),
    # path('loginbidder/', login_bidder, name='login_bidder'),
    # path('select-candidates', select_candidates, name='select_candidates'),
    path('upload-cv/<int:biddereg_id>', upload_cv, name='upload_cv'),

   
]

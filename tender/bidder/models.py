from django.db import models
from tenderapp.models import TenderReg
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class BidderReg(models.Model):
     # Define a list of regions in Tanzania
    REGION_CHOICES = [
        ('Arusha', 'Arusha'),
        ('Dar es Salaam', 'Dar es Salaam'),
        ('Dodoma', 'Dodoma'),
        ('Geita', 'Geita'),
        ('Iringa', 'Iringa'),
        ('Iringa3', 'Iringa3'),
        ('Iringa4', 'Iringa4'),
        # Add more regions as needed
    ]

    # Define a list of districts in Tanzania (example)
    DISTRICT_CHOICES = [
        ('Arusha', [
            ('Arusha City', 'Arusha City'),
            ('Arusha District', 'Arusha District'),
            # Add more districts in Arusha region as needed
        ]),
        ('Dar es Salaam', [
            ('Ilala', 'Ilala'),
            ('Kinondoni', 'Kinondoni'),
            # Add more districts in Dar es Salaam region as needed
        ]),
        ('Geita', [
            ('Ilala22', 'Ilala22'),
            ('Kinondoni66', 'Kinondoni66'),
            # Add more districts in Dar es Salaam region as needed
        ]),
        ('Dodoma', [
            ('Ilala33', 'Ilala33'),
            ('Kinondoni44', 'Kinondoni44'),
            # Add more districts in Dar es Salaam region as needed
        ]),
        # Add more regions and their districts as needed
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    companyName = models.CharField(max_length=255)
    tinNo = models.CharField(max_length=255)
    companyRegNo = models.CharField(max_length=255)
    vatNo = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    region = models.CharField(max_length=255, choices=REGION_CHOICES)
    district = models.CharField(max_length=255, choices=DISTRICT_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.CharField(max_length=255)
    business = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    foreignInput = models.CharField(max_length=255)
    employeeNum = models.CharField(max_length=255)
    passwords = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.companyName

    def clean(self):
        super().clean()
        if not self.phone.startswith('+255'):
            raise ValidationError('Phone number must start with "+255"')
        if len(self.phone) != 13:  # 4 characters for "+255" + 9 digits
            raise ValidationError('Phone number must have 9 digits following "+255"')

class bidapplication(models.Model):

        bidder= models.ForeignKey('BidderReg', on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
        time_to_complete = models.PositiveIntegerField( null=True, blank=True)
        tender = models.ForeignKey(TenderReg, on_delete=models.CASCADE,null=True, blank=True)



class SelectedBidder(models.Model):
    bidder = models.ForeignKey(BidderReg, on_delete=models.CASCADE)
    tender = models.ForeignKey(TenderReg, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cv/')

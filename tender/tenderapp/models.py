from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name =models.CharField(max_length=255, unique= True)

    def __str__(self):
        return self.name
    

class Bidder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional student fields as needed
    idNo=models.CharField(max_length=255)
    orgName=models.CharField(max_length=255)
    CATEGORY =[
        ('Private','Private'),
        ('Public','Public'),
        ('Government','Government')
    ]
    orgCategory=models.CharField(max_length=255,choices=CATEGORY)
    def __str__(self):
        return self.orgName

class CVDocument(models.Model):
    student = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    document = models.FileField(upload_to='cv_documents/')

class TenderReg(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add additional job position fields as needed
    tenderid = models.CharField(max_length=255,null=False, blank=True, primary_key=True)
    tender_name = models.CharField(max_length=255,null=True,blank=True)
    # cliendName =models.ForeignKey(ClientDetail,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    clinteId = models.CharField(max_length=255, blank=True, null=True)
    deadLineDate = models.DateField()
    procure_method = models.CharField(max_length=255)
    # STATU_TYPE =[
    #     ('Evaluated','Evaluated'),
    #     ('Bid Submission','Bid Submission'),
    #     ('Awarded','Awarded'),
    #     ('Canceled','Canceled')
    # ]
    # tender_status = models.CharField(max_length=255,choices=STATU_TYPE)
    financial_value = models.CharField(max_length=255)
  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.tenderid
    

    

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional teacher fields as needed


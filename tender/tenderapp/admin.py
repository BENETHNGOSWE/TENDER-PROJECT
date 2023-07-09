from django.contrib import admin
from .models import Bidder, CVDocument, TenderReg, Client,Category

admin.site.register(Bidder)
admin.site.register(CVDocument)
admin.site.register(TenderReg)
admin.site.register(Client)
admin.site.register(Category)

# Generated by Django 4.2.3 on 2023-07-09 14:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tenderapp', '0003_tenderreg_tender_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teacher',
            new_name='Client',
        ),
        migrations.RenameField(
            model_name='tenderreg',
            old_name='teacher',
            new_name='client',
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenderapp', '0002_bidder_category_tenderreg_remove_student_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenderreg',
            name='tender_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
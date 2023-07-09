# Generated by Django 4.2.3 on 2023-07-08 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenderapp', '0003_tenderreg_tender_name'),
        ('bidder', '0002_bidderreg_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedBidder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(upload_to='cv/')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidder.bidderreg')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenderapp.tenderreg')),
            ],
        ),
    ]
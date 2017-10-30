# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('prime3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawbillingrecord',
            name='UpdatedOn',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='NextVisitDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 10, 29, 19, 29, 31, 875131)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='PatientDateOfBirth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 10, 29, 19, 29, 31, 874854)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='PaymentDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 10, 29, 19, 29, 31, 874975)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='RegistrationDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 10, 29, 19, 29, 31, 874772)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='TimeOfBilling',
            field=models.TimeField(verbose_name=datetime.datetime(2017, 10, 29, 19, 29, 31, 874824)),
        ),
        migrations.AlterField(
            model_name='validatedbillingrecord',
            name='UpdatedOn',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 10, 29, 19, 29, 31, 875171)),
        ),
    ]

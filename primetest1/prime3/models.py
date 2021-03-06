from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class RawBillingRecord(models.Model):

    RecordID = models.AutoField(primary_key=True)
    ClientID = models.CharField(max_length=30,null=True)
    UHID =  models.CharField(max_length=30,null=True)
    AdmissionNumber = models.CharField(max_length=30,null=True)
    RegistrationDate = models.CharField(max_length=30,null=True)
    RegistrationNumber = models.CharField(max_length=30,null=True)
    BillingDate = models.CharField(max_length=30,null=True)
    BillingNumber = models.CharField(max_length=30,null=True) 
    TimeOfBilling = models.CharField(max_length=30,null=True)
    PatientZIP = models.CharField(max_length=30,null=True)
    PatientDateOfBirth = models.CharField(max_length=30,null=True)
    PatientGender = models.CharField(max_length=30,null=True)
    ServiceCode = models.CharField(max_length=30,null=True)
    ServiceName = models.CharField(max_length=30,null=True)
    NumberOfUnitsOfService = models.CharField(max_length=30,null=True)
    ServiceAmount = models.CharField(max_length=30,null=True)
    DoctorName = models.CharField(max_length=30,null=True)
    FinalBillAmount = models.CharField(max_length=30,null=True)
    FinalDiscountAmount = models.CharField(max_length=30,null=True)
    PaymentMode = models.CharField(max_length=30,null=True)
    PaymentAmount = models.CharField(max_length=30,null=True)
    PaymentDate = models.CharField(max_length=30,null=True)
    FinalBillingID = models.CharField(max_length=30,null=True)
    FinalEncounterID = models.CharField(max_length=30,null=True)
    InsuranceCoverage = models.CharField(max_length=30,null=True)
    EmployerBasedInsurance = models.CharField(max_length=30,null=True)
    InsuranceCompanyName = models.CharField(max_length=30,null=True)
    PatientEducation = models.CharField(max_length=30,null=True)
    EmploymentType = models.CharField(max_length=30,null=True)
    PatientEmployer = models.CharField(max_length=30,null=True)
    PatientAnnualIncomeRange = models.CharField(max_length=30,null=True)
    FrequencyOfGleneaglesVisit = models.CharField(max_length=30,null=True)
    LifestylePattern = models.CharField(max_length=30,null=True)
    TreatmentPlan = models.CharField(max_length=30,null=True)
    Rx = models.CharField(max_length=30,null=True)
    TestsPrescribed = models.CharField(max_length=30,null=True)
    NextVisitDate = models.CharField(max_length=30,null=True)
    Referrals = models.CharField(max_length=30,null=True)  
    UpdatedBy = models.CharField(max_length=30,null=True)
    UpdatedOn = models.CharField(max_length=30, null=True)


class ValidatedBillingRecord(models.Model):
    
    RecordID = models.IntegerField()
    ClientID = models.IntegerField()
    UHID =  models.IntegerField()
    AdmissionNumber = models.IntegerField()
    RegistrationDate =  models.DateTimeField(datetime.now())
    RegistrationNumber = models.IntegerField ()
    BillingDate = timezone.now()  
    BillingNumber = models.IntegerField () 
    TimeOfBilling = models.TimeField(datetime.now())
    PatientZIP = models.IntegerField ()
    PatientDateOfBirth = models.DateTimeField( datetime.now()) 
    PatientGender = models.CharField(max_length=30)
    ServiceCode = models.CharField(max_length=30)  
    ServiceName = models.CharField(max_length=30) 
    NumberOfUnitsOfService = models.IntegerField ()
    ServiceAmount = models.IntegerField ()
    DoctorName = models.CharField(max_length=30)  
    FinalBillAmount = models.IntegerField ()
    FinalDiscountAmount = models.IntegerField ()
    PaymentMode = models.CharField(max_length=30) 
    PaymentAmount = models.IntegerField (default=1)
    PaymentDate = models.DateTimeField(datetime.now())   
    FinalBillingID = models.IntegerField()
    FinalEncounterID = models.IntegerField()
    InsuranceCoverage = models.CharField(max_length=30) 
    EmployerBasedInsurance = models.CharField(max_length=30)
    InsuranceCompanyName = models.CharField(max_length=30)
    PatientEducation = models.CharField(max_length=30) 
    EmploymentType = models.CharField(max_length=30) 
    PatientEmployer = models.CharField(max_length=30) 
    PatientAnnualIncomeRange = models.IntegerField ()
    FrequencyOfGleneaglesVisit = models.CharField(max_length=30) 
    LifestylePattern = models.CharField(max_length=30) 
    TreatmentPlan = models.CharField(max_length=30)
    Rx = models.CharField(max_length=30) 
    TestsPrescribed = models.CharField(max_length=30) 
    NextVisitDate = models.DateTimeField(datetime.now())  
    Referrals = models.CharField(max_length=30) 
    UpdatedBy = models.CharField(max_length=30)
    UpdatedOn = models.DateTimeField(datetime.now())

class BadBillingRecord(models.Model):
  

    RecordID = models.IntegerField (null=True)
    ColumnName = models.CharField(max_length=30,null=True)
    ColumnValue = models.CharField(max_length=30,null=True)
    ErrorMessage = models.CharField(max_length=30,null=True)
    UpdatedOn = models.DateTimeField(default=datetime.now, null=True) 



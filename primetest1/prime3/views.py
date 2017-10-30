from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import RawBillingRecord,ValidatedBillingRecord,BadBillingRecord
from django.shortcuts import redirect,HttpResponse
#import json

from .datecheck import  datetimevalidation
from .billtime import timevalidater

#def validate():
#	return HttpResponse('Inside validate')

#def validate():
#	return -1

@api_view()
def primeDataExchangeAPI(request):
	import json
	api_response = {}

	if 'jsonBillingData' in request.GET:
		inputJSONstring = request.GET['jsonBillingData']
		inputJSONstring = str(inputJSONstring)
		received_json_data = json.loads(inputJSONstring)
		try:	
			s = RawBillingRecord(**received_json_data)
			s.save()
			 
			try:
				result = validate(received_json_data)
				

			except Exception as e :
				return HttpResponse(str(e))			

			if result == -1 :
				api_response['UHID'] = received_json_data.get('UHID')
				api_response['AdmissionNumber'] = received_json_data.get('AdmissionNumber')
				api_response['BillingNumber'] = received_json_data.get('BillingNumber')
				api_response['DataExchangeStatus'] = 'FAIL: Data Quality Errors Found'
				return Response(api_response)
			else:
				if '100' in received_json_data['ServiceCode']:
					return HttpResponse("Proceed to further process")
				else:
					return HttpResponse("100 not in the string")
		except Exception as e :
			

			api_response['UHID'] = received_json_data.get('UHID')
			api_response['AdmissionNumber'] = received_json_data.get('AdmissionNumber')
			api_response['BillingNumber'] = received_json_data.get('BillingNumber')
			api_response['DataExchangeStatus'] = 'FAIL: Wrong JSON Format Found'
			return Response(api_response)


def validate(received_json_data):
	returnvalue=0
	if received_json_data['RecordID'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='RecordID', ColumnValue=received_json_data['RecordID'])
		r.save()
		returnvalue=-1
	if received_json_data['UHID'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='UHID', ColumnValue=received_json_data['UHID'])
		r.save()
		returnvalue=-1
	if received_json_data['ClientID'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='ClientID', ColumnValue=received_json_data['ClientID'])
		r.save()
		returnvalue=-1        	
	if received_json_data['AdmissionNumber'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='AdmissionNumber', ColumnValue=received_json_data['AdmissionNumber'])
		r.save()
		returnvalue=-1          	 
	if datetimevalidation( received_json_data['RegistrationDate']):
		pass
	else:
		r=BadBillingRecord(ColumnName='RegistrationDate', ColumnValue=received_json_data['RegistrationDate'])
		r.save()
		returnvalue=-1 		 
	if received_json_data['RegistrationNumber'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='RegistrationNumber', ColumnValue=received_json_data['RegistrationNumber'])
		r.save()
		returnvalue=-1 	
	if datetimevalidation( received_json_data['BillingDate']):
		pass
	else:
		r=BadBillingRecord(ColumnName='BillingDate', ColumnValue=received_json_data['BillingDate'])
		r.save()
		returnvalue=-1 	 
	if received_json_data['BillingNumber'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='BillingNumber', ColumnValue=received_json_data['BillingNumber'])
		r.save()
		returnvalue=-1 	
	if timevalidater( received_json_data['TimeOfBilling']):
		pass
	else:
		r=BadBillingRecord(ColumnName='TimeOfBilling', ColumnValue=received_json_data['TimeOfBilling'])
		r.save()
		returnvalue=-1 	
	if received_json_data['PatientZIP'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='PatientZIP', ColumnValue=received_json_data['PatientZIP'])
		r.save()
		returnvalue=-1 
	if datetimevalidation( received_json_data['PatientDateOfBirth']):
		pass
	else:
		r=BadBillingRecord(ColumnName='PatientDateOfBirth', ColumnValue=received_json_data['PatientDateOfBirth'])
		r.save()
		returnvalue=-1 		
	if received_json_data['PatientGender']!="":
        	pass
	else:
		r=BadBillingRecord(ColumnName='PatientGender', ColumnValue=received_json_data['PatientGender'])
		r.save()
		returnvalue=-1 
	if received_json_data['ServiceCode']!="":
        	pass
	else:
		r=BadBillingRecord(ColumnName='ServiceCode', ColumnValue=received_json_data['ServiceCode'])
		r.save()
		returnvalue=-1 
	if received_json_data['ServiceName']!="":
        	pass
	else:
		r=BadBillingRecord(ColumnName='ServiceName', ColumnValue=received_json_data['ServiceName'])
		r.save()
		returnvalue=-1
	if received_json_data['NumberOfUnitsOfService'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='NumberOfUnitsOfService', ColumnValue=received_json_data['NumberOfUnitsOfService'])
		r.save()
		returnvalue=-1
	if received_json_data['ServiceAmount'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='ServiceAmount', ColumnValue=received_json_data['ServiceAmount'])
		r.save()
		returnvalue=-1
	if received_json_data['DoctorName']!="":
        	pass
	else:
		r=BadBillingRecord(ColumnName='DoctorName', ColumnValue=received_json_data['DoctorName'])
		r.save()
		returnvalue=-1
	if received_json_data['FinalBillAmount'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='FinalBillAmount', ColumnValue=received_json_data['FinalBillAmount'])
		r.save()
		returnvalue=-1
	if received_json_data['FinalDiscountAmount'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='FinalDiscountAmount', ColumnValue=received_json_data['FinalDiscountAmount'])
		r.save()
		returnvalue=-1
	if received_json_data['PaymentMode']!="":
        	pass
	else:
		r=BadBillingRecord(ColumnName='PaymentMode', ColumnValue=received_json_data['PaymentMode'])
		r.save()
		returnvalue=-1
	if received_json_data['PaymentAmount'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='PaymentAmount', ColumnValue=received_json_data['PaymentAmount'])
		r.save()
		returnvalue=-1
	if datetimevalidation( received_json_data['PaymentDate']):
		pass
	else:
		r=BadBillingRecord(ColumnName='PaymentDate', ColumnValue=received_json_data['PaymentDate'])
		r.save()
		returnvalue=-1
	if received_json_data['FinalBillingID'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='FinalBillingID', ColumnValue=received_json_data['FinalBillingID'])
		r.save()
		returnvalue=-1
	if received_json_data['FinalEncounterID'].isnumeric():
        	pass
	else:
		r=BadBillingRecord(ColumnName='FinalEncounterID', ColumnValue=received_json_data['FinalEncounterID'])
		r.save()
		returnvalue=-1
#	if received_json_data['InsuranceCoverage']!="":
#        	pass
#	else:
#		r=BadBillingRecord(ColumnName='InsuranceCoverage', ColumnValue=received_json_data['InsuranceCoverage'])
#		r.save()
#		returnvalue=-1
#	if received_json_data['EmployerBasedInsurance']!="":
#       	pass
#	else:
#		r=BadBillingRecord(ColumnName='EmployerBasedInsurance', ColumnValue=received_json_data['EmployerBasedInsurance'])
#		r.save()
#		returnvalue=-1
#	if received_json_data['InsuranceCompanyName']!="":
#        	pass
#	else:
#		r=BadBillingRecord(ColumnName='InsuranceCompanyName', ColumnValue=received_json_data['InsuranceCompanyName'])
#		r.save()
#		returnvalue=-1
#	if received_json_data['PatientEducation']!="":
#       	pass
#	else:
#		r=BadBillingRecord(ColumnName='PatientEducation', ColumnValue=received_json_data['PatientEducation'])
#		r.save()
#		returnvalue=-1
#	if received_json_data['EmploymentType']!="":
#       	pass
#	else:
#		r=BadBillingRecord(ColumnName='EmploymentType', ColumnValue=received_json_data['EmploymentType'])
#		r.save()
#		returnvalue=-1
#	if received_json_data['PatientEmployer']!="":
#       	pass
#	else:
#		r=BadBillingRecord(ColumnName='PatientEmployer', ColumnValue=received_json_data['PatientEmployer'])
#		r.save()
#		returnvalue=-1
#	if received_json_data['PatientAnnualIncomeRange'].isnumeric():
#       	pass
#	else:
#		r=BadBillingRecord(ColumnName='PatientAnnualIncomeRange', ColumnValue=received_json_data['PatientAnnualIncomeRange'])
#		r.save()
#		returnvalue=-1
#	if received_json_data['FrequencyOfGleneaglesVisit']!="":
#       	pass
#	else:
#		r=BadBillingRecord(ColumnName='FrequencyOfGleneaglesVisit', ColumnValue=received_json_data['FrequencyOfGleneaglesVisit'])
#		r.save()
#		returnvalue=-1		
#	if received_json_data['LifestylePattern']!="":
#       	pass
#	else:
#		r=BadBillingRecord(ColumnName='LifestylePattern', ColumnValue=received_json_data['LifestylePattern'])
#		r.save()
#		returnvalue=-1		
#	if received_json_data['TreatmentPlan']!="":
#        	pass
#	else:
#		r=BadBillingRecord(ColumnName='TreatmentPlan', ColumnValue=received_json_data['TreatmentPlan'])
#		r.save()
#		returnvalue=-1
#	if received_json_data['Rx']!="":
#       	pass
#	else:
#		r=BadBillingRecord(ColumnName='Rx', ColumnValue=received_json_data['Rx'])
#		r.save()
#		returnvalue=-1
#	if received_json_data['TestsPrescribed']!="":
#        	pass
#	else:
#		r=BadBillingRecord(ColumnName='TestsPrescribed', ColumnValue=received_json_data['TestsPrescribed'])
#		r.save()
#		returnvalue=-1		
#	if datetimevalidation( received_json_data['NextVisitDate']):
#		pass
#	else:
#		r=BadBillingRecord(ColumnName='NextVisitDate', ColumnValue=received_json_data['NextVisitDate'])
#		r.save()
#		returnvalue=-1	
#	if received_json_data['Referrals']!="":
#        	pass
#	else:
#		r=BadBillingRecord(ColumnName='Referrals', ColumnValue=received_json_data['Referrals'])
#		r.save()
#		returnvalue=-1	
	if received_json_data['UpdatedBy']!="":
        	pass
	else:
		r=BadBillingRecord(ColumnName='UpdatedBy', ColumnValue=received_json_data['UpdatedBy'])
		r.save()
		returnvalue=-1	
        	 
	if datetimevalidation( received_json_data['UpdatedOn']):
		pass
	else:
		r=BadBillingRecord(ColumnName='UpdatedOn', ColumnValue=received_json_data['UpdatedOn'])
		r.save()
		returnvalue=-1	
		

	return returnvalue	

	

	

	

					 
        
		

#	obj=RawBillingRecord.objects.latest('RecordID')
	#p= ValidatedBillingRecord(**received_json_data)
	#p.save()						





		
		
		
		


		

		





		

# Create your views here.

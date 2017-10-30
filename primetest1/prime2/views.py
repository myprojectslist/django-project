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
				return HttpResponse(result)

			except Exception as e :
				return HttpResponse(str(e))			

			if result == -1 :
				api_response['UHID'] = received_json_data.get('UHID')
				api_response['AdmissionNumber'] = received_json_data.get('AdmissionNumber')
				api_response['BillingNumber'] = received_json_data.get('BillingNumber')
				api_response['DataExchangeStatus'] = 'FAIL: Data Quality Errors Found'
				return Response(api_response)
			else:
				return HttpResponse("Proceed to further process")

		except Exception as e :
			return HttpResponse(str(e))

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
        	returnvalue=-1
	if received_json_data['ClientID'].isnumeric():
        	pass
	else:
        	returnvalue=-1
	if received_json_data['AdmissionNumber'].isnumeric():
        	pass
	else:
        	returnvalue=-1
	if datetimevalidation( received_json_data['RegistrationDate']):
		pass
	else:
		returnvalue=-1
	if received_json_data['RegistrationNumber']!="":
        	pass
	else:
        	returnvalue=-1
	if datetimevalidation( received_json_data['BillingDate']):
		pass
	else:
		returnvalue=-1
	if received_json_data['BillingNumber'].isnumeric():
        	pass
	else:
		returnvalue=-1
	if timevalidater( received_json_data['TimeOfBilling']):
		pass
	else:
		returnvalue=-1
	if received_json_data['PatientZIP'].isnumeric():
        	pass
	else:
        	returnvalue=-1
	if datetimevalidation( received_json_data['PatientDateOfBirth']):
		pass
	else:
		returnvalue=-1
	if received_json_data['PatientGender'].isnumeric():
        	pass
	else:
        	returnvalue=-1
	if received_json_data['ServiceCode']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['ServiceName']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['NumberOfUnitsOfService'].isnumeric():
        	pass
	else:
		returnvalue=-1
	if received_json_data['ServiceAmount'].isnumeric():
        	pass
	else:
		returnvalue=-1
	if received_json_data['DoctorName']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['FinalBillAmount'].isnumeric():
        	pass
	else:
		returnvalue=-1
	if received_json_data['FinalDiscountAmount'].isnumeric():
        	pass
	else:
		returnvalue=-1
	if received_json_data['PaymentMode']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['PaymentAmount'].isnumeric():
        	pass
	else:
		returnvalue=-1
	if datetimevalidation( received_json_data['PaymentDate']):
		pass
	else:
		returnvalue=-1
	if received_json_data['FinalBillingID'].isnumeric():
        	pass
	else:
		returnvalue=-1
	if received_json_data['FinalEncounterID'].isnumeric():
        	pass
	else:
		returnvalue=-1
	if received_json_data['InsuranceCoverage']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['EmployerBasedInsurance']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['InsuranceCompanyName']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['PatientEducation']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['EmploymentType']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['PatientEmployer']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['PatientAnnualIncomeRange'].isnumeric():
        	pass
	else:
		returnvalue=-1
	if received_json_data['FrequencyOfGleneaglesVisit']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['LifestylePattern']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['TreatmentPlan']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['Rx']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['TestsPrescribed']!="":
        	pass
	else:
        	returnvalue=-1
	if datetimevalidation( received_json_data['NextVisitDate']):
		pass
	else:
		returnvalue=-1
	if received_json_data['Referrals']!="":
        	pass
	else:
        	returnvalue=-1
	if received_json_data['UpdatedBy']!="":
        	pass
	else:
        	returnvalue=-1
	if datetimevalidation( received_json_data['UpdatedOn']):
		pass
	else:
		returnvalue=-1

	return returnvalue	

	

	

	

					 
        
		

#	obj=RawBillingRecord.objects.latest('RecordID')
	#p= ValidatedBillingRecord(**received_json_data)
	#p.save()						





		
		
		
		


		

		





		

# Create your views here.

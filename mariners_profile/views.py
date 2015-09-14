from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404

from login.models import UserProfile
from . models import *

from application_form.forms import FlagForm, TrainingCertificateForm, StatusForm

# Create your views here.
@login_required()
def index(request):
	user = UserProfile.objects.get(user=request.user)
	name = "%s %s %s" % (user.first_name, user.middle_name, user.last_name )
	mariners_profile = MarinersProfile.objects.filter(status=1)
	counter = 0
	count = list()
	rank = list()
	age = list()
	vessel_type = list()
	mobile_1 = list()
	email_address_1 = list()


	for mariners in mariners_profile:
		# mariners.user - to return the UserProfile instance
		count.append(1)
		rank.append(mariners.position)
		age.append(PersonalData.objects.get(name=mariners.user).age)
		vessel_type.append(PersonalData.objects.get(name=mariners.user).preferred_vessel_type)
		mobile_1.append(PersonalData.objects.get(name=mariners.user).mobile_1)
		email_address_1.append(PersonalData.objects.get(name=mariners.user).email_address_1)

	zipped_data = zip(count, mariners_profile, rank, age, vessel_type, mobile_1, email_address_1)

	print count

	template = "mariner-profile/index.html"
	context_dict = {"title": "Mariners Profile"}
	# [0] is put to break the instance into the unicode value
	try:
		context_dict['rank'] = rank
		context_dict['age'] = age
		context_dict['vessel_type'] = vessel_type
		context_dict['mobile_1'] = mobile_1
		context_dict['email_address_1'] = email_address_1
		context_dict['mariners_profile'] = mariners_profile
		context_dict['name'] = name
		context_dict['zipped_data'] = zipped_data
		context_dict['count'] = count
	except:
		pass
	return render(request, template, context_dict)

@login_required()
def profile(request, id):
	if id:
		user_profile = UserProfile.objects.get(id=id)
		personal_data = PersonalData.objects.get(name=id)
		try:
			spouse = Spouse.objects.get(user=id)
		except:
			spouse = ''
		college = College.objects.filter(user=id)
		highschool = HighSchool.objects.get(user=id)
		emergency_contact = EmergencyContact.objects.filter(user=id)
		visa_application = VisaApplication.objects.get(user=id)
		detained = Detained.objects.get(user=id)
		disciplinary_action = DisciplinaryAction.objects.get(user=id)
		charged_offense = ChargedOffense.objects.get(user=id)
		termination = Termination.objects.get(user=id)
		passport = Passport.objects.get(user=id)
		sbook = Sbook.objects.get(user=id)
		coc = COC.objects.get(user=id)
		license = License.objects.get(user=id)
		src = SRC.objects.get(user=id)
		goc = GOC.objects.get(user=id)
		us_visa = USVisa.objects.get(user=id)
		schengen_visa = SchengenVisa.objects.get(user=id)
		yellow_fever = YellowFever.objects.get(user=id)
		# FlagDocuments = FlagDocuments.objects.get(user=id)
		# FlagDocumentsDetailed = FlagDocumentsDetailed.objects.get(user=id)
		# TrainingCertificateDocuments = TrainingCertificateDocuments.objects.get(user=id)
		# TrainingCertificateDocumentsDetailed = TrainingCertificateDocumentsDetailed.objects.get(user=id)
		sea_service = SeaService.objects.filter(user=id)
		mariners_profile = MarinersProfile.objects.get(user=id)

		try:
			flag_documents = FlagDocuments.objects.get(user=user_profile)
			flag_list = []
			flags = get_list_or_404(FlagDocumentsDetailed, flags_documents=flag_documents.id)
			# print flags
			for flag in flags:
				# print flag.id
				flag_list.append(flag.flags.id)
			flags = {'flags': flag_list}
			flags = FlagForm(initial=flags)
		except:
			flags = ''

		training_certificate_documents = TrainingCertificateDocuments.objects.get(user=user_profile)
		training_certificate_list = []
		training_certificates = get_list_or_404(TrainingCertificateDocumentsDetailed, trainings_certificate_documents=training_certificate_documents.id)
		# print training_certificates
		for training_certificate in training_certificates:
			# print training_certificate.id
			# print training_certificate.trainings_certificates.id
			training_certificate_list.append(training_certificate.trainings_certificates.id)
		training_certificates = {'trainings_certificates': training_certificate_list}
		trainings_certificates = TrainingCertificateForm(initial=training_certificates)

		template = "mariner-profile/profile.html"

		context_dict = {}
		context_dict['user_profile'] = user_profile
		context_dict['personal_data'] = personal_data
		context_dict['spouse'] = spouse
		context_dict['college'] = college
		context_dict['highschool'] = highschool
		context_dict['emergency_contact'] = emergency_contact
		context_dict['visa_application'] = visa_application
		context_dict['detained'] = detained
		context_dict['disciplinary_action'] = disciplinary_action
		context_dict['charged_offense'] = charged_offense
		context_dict['termination'] = termination
		context_dict['passport'] = passport
		context_dict['sbook'] = sbook
		context_dict['coc'] = coc
		context_dict['license'] = license
		context_dict['src'] = src
		context_dict['goc'] = goc
		context_dict['us_visa'] = us_visa
		context_dict['schengen_visa'] = schengen_visa
		context_dict['yellow_fever'] = yellow_fever
		context_dict['title'] = "Mariners Profile - "+str(personal_data)
		# context_dict['FlagDocuments'] = FlagDocuments
		# context_dict['FlagDocumentsDetailed'] = FlagDocumentsDetailed
		# context_dict['TrainingCertificateDocuments'] = TrainingCertificateDocuments
		# context_dict['TrainingCertificateDocumentsDetailed'] = TrainingCertificateDocumentsDetailed
		context_dict['sea_service'] = sea_service
		context_dict['mariners_profile'] = mariners_profile

		context_dict['flags'] = flags
		context_dict['trainings_certificates'] = trainings_certificates

		return render(request, template, context_dict)
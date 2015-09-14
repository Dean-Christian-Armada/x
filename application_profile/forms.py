from django import forms

import autocomplete_light

from mariners_profile.models import MarinersProfile

class MarinersDataTables(autocomplete_light.ModelForm):
	# search = autocomplete_light.GenericModelChoiceField('FlagAutocomplete')
	user = autocomplete_light.ModelChoiceField('FlagAutocomplete')

	class Meta:
		model = MarinersProfile
		# autocomplete_fields = ('user', )
		fields = ('user', )
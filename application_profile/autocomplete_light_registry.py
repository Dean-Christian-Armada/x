from mariners_profile.models import MarinersProfile, Flags

import autocomplete_light


# class ApplicantsAutocomplete(autocomplete_light.AutocompleteModelTemplate):
#     choices = (
#     	Flags.objects.all()
#     	)

#    	search_fields = (
#    		('flags'), 
#    		)
#     # search_fields = ['^position', ]
#     # model = MarinersProfile
#     # search_fields = ['^flags', ]
#     # model = Flags
#     # Template that removes the "Results not Found"
#     autocomplete_template = 'autocomplete_template.html'
    
# autocomplete_light.register(ApplicantsAutocomplete)
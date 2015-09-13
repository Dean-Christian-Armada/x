from mariners_profile.models import ReferrersPool

import autocomplete_light


class ReferrerAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    search_fields = ['^name', ]
    model = ReferrersPool
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
    
autocomplete_light.register(ReferrerAutocomplete)
from django.contrib import admin
from .models import Welcome, Specialization, SpecializationItem, OurRecentProjectsItem, OurRecentProjects, Team, \
    OurStory, WhatWeOfferObjects, WhatWeOffer, Services, Services_heading, ContactInfo,ClientSection

# Register your models here.


admin.site.register(Welcome)
admin.site.register(Specialization)
admin.site.register(SpecializationItem)
admin.site.register(OurRecentProjects)
admin.site.register(OurRecentProjectsItem)
admin.site.register(Team)
admin.site.register(OurStory)
admin.site.register(WhatWeOfferObjects)
admin.site.register(WhatWeOffer)
admin.site.register(Services_heading)
admin.site.register(Services)
admin.site.register(ContactInfo)
admin.site.register(ClientSection)
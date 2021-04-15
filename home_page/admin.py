from django.contrib import admin
from .models import Application, WelcomeWords, MissionVision, Slider, HeadingOne, HeadingTwo, HeadingThree
from about.models import Director, AboutUs, TeamDescription, Team
from gallery.models import GallerySlider, Gallery, GalleryExtra
from muslim_school.models import  Sliding, HeaderOne, HeaderTwo, ApplicationForm, Welcome, Achievers, Staff
from online_library.models import Library
from Projects.models import Project
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Application)
admin.site.register(WelcomeWords)
admin.site.register(MissionVision)
admin.site.register(Slider)
admin.site.register(HeadingOne)
admin.site.register(HeadingTwo)
admin.site.register(HeadingThree)

admin.site.register(Director)
admin.site.register(AboutUs)
admin.site.register(TeamDescription)
admin.site.register(Team)

admin.site.register(GallerySlider)
admin.site.register(Gallery)
admin.site.register(GalleryExtra)

admin.site.register(Sliding)
admin.site.register(HeaderOne)
admin.site.register(HeaderTwo)
admin.site.register(ApplicationForm)
admin.site.register(Welcome)
admin.site.register(Achievers)
admin.site.register(Staff)

admin.site.register(Library)
admin.site.register(Project, MyModelAdmin)




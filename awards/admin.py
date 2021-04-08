from django.contrib import admin
from .models import Profile,Project,MoringaMerch,AwardsProject

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
# admin.site.register(Like)
# admin.site.register(Comment)
# admin.site.register(DisLike)
admin.site.register(MoringaMerch)
admin.site.register(AwardsProject)

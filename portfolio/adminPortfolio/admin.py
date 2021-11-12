from django.contrib import admin

# Register your models here.
from adminPortfolio.models import UserInfo, Formation, Competence, Experience

admin.site.register(UserInfo)
admin.site.register(Formation)
admin.site.register(Competence)
admin.site.register(Experience)
from django.contrib import admin

from app_api.models import (
                        Course,
                        Branch,
                        Contact,
                    )

admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Contact)

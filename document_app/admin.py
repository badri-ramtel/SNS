from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from document_app.models import Laws, References, Appreciations, Registrations, Program_Registrations

# Register your models here.
admin.site.register(Laws)
admin.site.register(References)
admin.site.register(Appreciations)
admin.site.register(Registrations)

class ProgramAdmin(admin.ModelAdmin):
    list_display = ['participant_full_name', 'age', 'address', 'your_contact', 'your_email', 'parents_full_name', 'parents_contact', 'program', 'status']
    actions = ['take_action']

    def take_action(self, request, queryset):
        updated = queryset.update(status= "C")
        self.message_user(
            request,
            ngettext(
                "%d Program was successfully marked as Confirmed.",
                "%d Programs were successfully marked as Confirmed.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

admin.site.register(Program_Registrations, ProgramAdmin)

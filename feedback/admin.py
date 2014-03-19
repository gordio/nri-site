from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'email',  )
    readonly_fields = ('email', 'pub_date', 'content', )


admin.site.register(Message, MessageAdmin)
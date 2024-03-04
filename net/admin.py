from django.contrib import admin
from net.models import NetElement
from net.services import clear_debt


@admin.register(NetElement)
class NetElementAdmin(admin.ModelAdmin):
    """
    Админка для товаров
    """

    list_display = ('title', 'business_form', 'city', 'provider', 'debt',)
    list_filter = ('country', 'city',)
    list_display_links = ('title', 'provider',)
    actions = [clear_debt]

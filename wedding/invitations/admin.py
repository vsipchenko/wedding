from django.contrib import admin
from django.contrib.sites.models import Site
from django.utils.html import format_html

from .models import Invitation


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('is_approved', 'created_at', 'updated_at')
    list_display = ('name', 'is_approved', 'share', 'link')

    def _get_invitation_url(self, obj):
        site = Site.objects.get_current()
        return f'http://{site.domain}{obj.detail_url}'

    def share(self, obj):
        url = self._get_invitation_url(obj)
        telegram_url = f'https://telegram.me/ashare/url?url={url}'
        viber_url = f'http://viber://forward?text={url}'
        return format_html(
            f'<a class="button" href={telegram_url}>Telegram</a>&nbsp;'
            f'<a class="button" href={viber_url}>Viber</a>'
        )
    share.short_description = 'Share via'

    def link(self, obj):
        url = self._get_invitation_url(obj)
        return format_html(f'<a class="button" href="{url}">Link</a>')

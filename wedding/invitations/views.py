from django.core.exceptions import ValidationError
from django.utils import timezone
from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Invitation

class InvitationDetailView(DetailView):
    queryset = Invitation.objects.only('id', 'name', 'is_approved')
    template_name = 'invitations/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

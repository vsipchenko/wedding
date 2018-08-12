from django.urls import path

from .views import InvitationDetailView

app_name = 'invitations'

urlpatterns = [
    path('invitation/<uuid:pk>/', InvitationDetailView.as_view(), name='detail'),
]

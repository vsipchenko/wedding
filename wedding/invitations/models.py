import uuid

from django.db import models


class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    is_approved = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invitation recipient - {self.name}"

    @property
    def detail_url(self):
        from django.urls import reverse
        return reverse('invitations:detail', args=[self.id])

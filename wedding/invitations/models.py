import uuid

from django.db import models


class Invitation(models.Model):
    MALE = 0
    FEMALE = 1
    PAIR = 2
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (PAIR, 'Pair')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invitation recipient - {self.name}"

    @property
    def detail_url(self):
        from django.urls import reverse
        return reverse('invitations:detail', args=[self.id])

    @property
    def gender_address(self):
        address = {
            self.MALE: 'Дорогой',
            self.FEMALE: 'Дорогая',
            self.PAIR: 'Дорогие'
        }
        return address.get(self.gender)

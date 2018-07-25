from django.db import models
from django.utils import timezone


class SelectScent(models.Model):
    client = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    scent = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    select_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.select_date = timezone.now()
        self.save()

    def __str__(self):
        return self.scent

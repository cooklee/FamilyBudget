from django.db import models

# Create your models here.


class SafeRecord(models.Model):

    base_url = models.URLField()
    password = models.CharField(max_length=8)
    random_url = models.URLField()

    def generate_url(self):


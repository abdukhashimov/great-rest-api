from django.db import models


class InfoModel(models.Model):
    name = models.CharField(max_length=255)
    information = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

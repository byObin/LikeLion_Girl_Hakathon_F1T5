from django.db import models

class PWtest(models.Model):
    pw = models.IntegerField(max_length=8)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.title
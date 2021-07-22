from django.db import models


class emp(models.Model):
    e_name = models.CharField(max_length = 20)
    e_id = models.IntegerField()
    email = models.EmailField(max_length = 20)
    pas = models.CharField(max_length = 20)

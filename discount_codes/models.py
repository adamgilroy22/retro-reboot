from django.db import models


class DiscountCode(models.Model):
    code = models.CharField(max_length=20, null=False,
                            blank=False, unique=True)
    discount = models.IntegerField(null=False, blank=False)

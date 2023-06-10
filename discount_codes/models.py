from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class DiscountCode(models.Model):
    code = models.CharField(max_length=20, null=False,
                            blank=False, unique=True)
    discount = models.IntegerField(null=False, blank=False, validators=[
            MaxValueValidator(99),
            MinValueValidator(1)
        ])

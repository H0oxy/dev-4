from django.db import models

class Numbers(models.Model):
    numbers = models.TextField(verbose_name='Число')

    class Meta:
        verbose_name = 'Число'
        verbose_name_plural = 'Числа'

from django.db import models


class Model(models.Model):
    field = models.CharField(verbose_name="Field", max_length=255)

    class Meta:
        ordering = ["field"]
        verbose_name = "Field"
        verbose_name_plural = "Fields"

    def __str__(self):
        return f"{self.field}"

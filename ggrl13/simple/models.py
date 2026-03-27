from django.db import models

# Create your models here.

class FormDataModel(models.Model):
    inputs = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'form_data'
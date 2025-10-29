# result/models.py

from django.db import models
from django.core.exceptions import ValidationError

# ✅ Validator function
def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError("Only PDF files are allowed.")

# ✅ Model
class Attachment(models.Model):
    title = models.CharField(max_length=255)
    discrip = models.CharField(max_length=500)
    attachment = models.FileField(
        upload_to='attachments/',
        blank=True,
        null=True,
        validators=[validate_pdf]  # no import needed
    )

    def __str__(self):
        return self.title

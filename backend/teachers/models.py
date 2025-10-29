from django.db import models

class TeacherJson(models.Model):  
    teacher_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    teacher_password = models.CharField(max_length=100, default='password123')
    teacher_email = models.EmailField(max_length=100, default='example@email.com')
    teacher_phone = models.CharField(max_length=15, default='0000000000')
    teacher_address = models.CharField(max_length=255, default='noaddress')
    details = models.TextField()
    image = models.ImageField(upload_to='teacher/', blank=True, null=True)

    def __str__(self):
        return self.teacher_name

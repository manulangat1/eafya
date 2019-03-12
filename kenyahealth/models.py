from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    doctor_no = models.PositiveIntegerField()
    def __str__(self):
        return self.user.username
    def save_doctor(self):
        self.save()
class History(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    by = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    def __str__(self):
        return self.text
    def save_hist(self):
        self.save()
class Patient(models.Model):
    name = models.CharField(max_length=89)
    age = models.PositiveIntegerField()
    patient_no = models.PositiveIntegerField(unique=True)
    id_no = models.PositiveIntegerField(unique=True)
    history = models.ForeignKey(History,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def save_pati(self):
        self.save()

from rest_framework import serializers
from .models import Doctor,Patient,History
from django.contrib.auth.models import User
from .tasks import send_welcome_email_task
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('text','created_at','by',)
class PatientSerializer(serializers.ModelSerializer):
    history = HistorySerializer()
    class Meta:
        model = Patient
        fields = ('name','age','patient_no','id_no','history',)
    def create(self,validated_data):
        history = validated_data.pop('history')
        history = History.objects.create(**history)
        patient = Patient.objects.create(history=history,**validated_data)
        return patient
    def update(self,instance,validated_data):
        history = validated_data.pop('history')
        hist = instance.history
        hist.text =  history.get('text',hist.text)
        hist.save()
        return instance
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {"password":{'write_only':True}}
    def create(self,validated_data):
        username = validated_data['username']
        email = validated_data['email']
        user = User(username=username,email=email)
        user.set_password(validated_data['password'])
        user.save()
        send_welcome_email_task.delay(username,email)
        return user

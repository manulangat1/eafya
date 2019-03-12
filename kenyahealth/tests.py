from django.test import TestCase
from .models import Doctor,Hospital,History,Patient
from django.contrib.auth.models import User
# Create your tests here.
class DoctorTestClass(TestCase):
    def setUp(self):
        self.manu = User(username='manu',email='langatfarmer@gmail.com')
        self.manu.set_password('3050manu')
        self.manu.save()
        self.manulangat = Doctor(user=self.manu,doctor_no=4689)
        self.manulangat.save()
    def test_instance(self):
        assertTrue(isinstance(self.manulangat,Doctor))
    def test_save_doctor(self):
        self.manulangat.save_doctor()
        doc = Doctor.objects.all()
        assertTrue(len(doc) > 0 )
    def tearDown(self):
        User.objects.all().delete()
        Doctor.objects.all().delete()
class HistoryTestClass(TestCase):
    def setUp(self):
        self.manu = User(username='manu',email='langatfarmer@gmail.com')
        self.manu.set_password('3050manu')
        self.manu.save()
        self.manulangat = Doctor(user=self.manu,doctor_no=4689)
        self.manulangat.save()
        self.hist = History(text='helo there',by=self.manulangat)
        self.hist.save()
    def test_instance(self):
        assertTrue(isinstance(self.hist,History))
    def test_save_hist(self):
        self.hist.save_hist()
        hist = History.objects.all()
        assertTrue(len(hist) > 0)
    def tearDown(self):
        User.objects.all().delete()
        Doctor.objects.all().delete()
        History.objects.all().delete()
class PatientTestClass(TestCase):
    def setUp(self):
        self.manu = User(username='manu',email='langatfarmer@gmail.com')
        self.manu.set_password('3050manu')
        self.manu.save()
        self.manulangat = Doctor(user=self.manu,doctor_no=4689)
        self.manulangat.save()
        self.hist = History(text='helo there',by=self.manulangat)
        self.hist.save()
        self.pat = Patient(name='emmanuel',age=48,patient_no=6702,id_no=35903423,history=self.hist)
        self.pat.save()
    def test_instance(self):
        assertTrue(isinstance(self.pat,Patient))
    def test_save_pati(self):
        self.pat.save_pati()
        pati = Patient.objects.all()
        assertTrue(len(pati) > 0)
    def tearDown(self):
        User.objects.all().delete()
        Doctor.objects.all().delete()
        History.objects.all().delete()
        Patient.objects.all().delete()

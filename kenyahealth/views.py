from django.shortcuts import render
from .models import Doctor,Patient,History
from .serializers import PatientSerializer,DoctorSerializer,HistorySerializer,UserSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login,authenticate,logout
from .tasks import send_history_email_task
# Create your views here.
def index(request):
    return render(request,'index.html')
class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
class LoginView(APIView):
    def post(self,request,format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        send_history_email_task(username,email)
        user = authenticate(username=username,password=password)
        if user:
            return Response(login(request,user))
        else:
            return Response({"error": "wrong credential"},status=status.HTTP_400_BAD_REQUEST)
class LogoutView(APIView):
    def post(self,request,format=None):
        return Response(logout(request,user))

from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView


class StudentAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]

    def get(self,request):
        stu_data= Student.objects.all()
        serialize_org = StudentSerializer(stu_data,many=True)
        return Response(serialize_org.data)
    
    def post(self,request):
        stu_data = StudentSerializer(data = request.data)
        if stu_data.is_valid():
            stu_data.save()
            return Response(stu_data.data,status = status.HTTP_201_CREATED)
        return Response(stu_data.errors,status = status.HTTP_400_BAD_REQUEST)

class StudentDetailsBy_ID(APIView):
   
    def get_object(self,id):
        try:
            return Student.objects.get(id = id)
        except Student.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        stu_data = self.get_object(id)
        serialize_org = StudentSerializer(stu_data) 
        return Response(serialize_org.data)
    
    def put(self,request,id):
        stu_data = self.get_object(id)
        serialize_org = StudentSerializer(stu_data, data = request.data)
        if serialize_org.is_valid():
            serialize_org.save()
            return Response(serialize_org.data)
        return Response(serialize_org.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        stu_data = self.get_object(id)
        stu_data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
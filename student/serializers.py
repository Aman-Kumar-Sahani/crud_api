from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Student

class StudentSerializer(DocumentSerializer):
    class Meta:
        model = Student
        fields = '__all__'

from rest_framework import status
from rest_framework.response import Response
from core.serializers import  (
    CollegeSerializer,
    TeacherCreateUpdateSerializer,
    TeacherGetSerializer,
    StudentCreateUpdateSerializer,
    StudentGetSerializer
)
from core.models import Student
from core.utils import general_message
from .student_base_services import StudentBaseService



class StudentService(StudentBaseService):
    def __init__(self):
        pass

    def create(self, request, format=None):
        """Create Student."""
        try:
            serializer = StudentCreateUpdateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.CREATED})
            else:
                return Response({'data': None, 'code': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})

    def get(self, request, pk, format=None):
        """Get Student."""
        try:
            try:
                student = Student.objects.get(id=pk)
                serializer = StudentGetSerializer(student)
                return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.RETRIEVED})
            except:
                return Response({'data': None, 'code': status.HTTP_204_NO_CONTENT, 'message': general_message.RECORD_NOT_FOUND})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})
        
    def get_list(self, request, format=None):
        """Get Student list."""
        try:
            try:
                student = Student.objects.all()
                serializer = StudentGetSerializer(student, many=True)
                return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.RETRIEVED})
            except:
                return Response({'data': None, 'code': status.HTTP_204_NO_CONTENT, 'message': general_message.RECORD_NOT_FOUND})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})

    def update(self, request, pk, format=None):
        """Update Student."""
        try:
            try:
                student = Student.objects.get(id=pk)
                serializer = StudentCreateUpdateSerializer(student, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.UPDATED})
                else:    
                    return Response({'data': None, 'code': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})
            except:
                return Response({'data': None, 'code': status.HTTP_204_NO_CONTENT, 'message': general_message.RECORD_NOT_FOUND})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})
        
    def delete(self, request, pk, format=None):
        """Delete Student."""
        try:
            try:
                student = Student.objects.get(id=pk)
                student.delete()
                return Response({'data':{}, 'code':status.HTTP_200_OK, 'message':general_message.DELETE})
            except:
                return Response({'data':None, 'code':status.HTTP_204_NO_CONTENT, 'message':general_message.RECORD_NOT_FOUND})
        except Exception as e:
            return Response({'data':None, 'code':status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})
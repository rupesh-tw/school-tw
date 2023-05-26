from rest_framework import status
from rest_framework.response import Response
from core.serializers import CollegeSerializer, StudentSerializer
from core.utils import general_message
from .student_base_services import StudentBaseService


class StudentService(StudentBaseService):
    def __init__(self):
        pass

    def create_update(self, request, format=None):
        """Create college."""
        try:
            serializer = StudentSerializer(data = request.data)
            if serializer.is_valid():
                return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.CREATED})
            else:
                return Response({'data': None, 'code': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})
                
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})
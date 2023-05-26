from rest_framework import status
from rest_framework.response import Response
from core.serializers import (
    CollegeSerializer, 
    TeacherGetSerializer,
    TeacherCreateUpdateSerializer
)
    
from core.models import Teacher
from core.utils import general_message
from .teacher_base_services import TeacherBaseService


class TeacherService(TeacherBaseService):
    def __init__(self):
        pass

    def create(self, request, format=None):
        """Create Teacher."""
        try:
            serializer = TeacherCreateUpdateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.CREATED})
            else:
                return Response({'data': None, 'code': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})

    def get(self, request, pk, format=None):
        """Get Teacher."""
        try:
            try:
                teacher = Teacher.objects.get(id=pk)
                serializer = TeacherGetSerializer(teacher)
                return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.RETRIEVED})
            except:
                return Response({'data': None, 'code': status.HTTP_204_NO_CONTENT, 'message': general_message.RECORD_NOT_FOUND})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})
        
    def get_list(self, request, format=None):
        """Get Teacher list."""
        try:
            try:
                teacher = Teacher.objects.all()
                serializer = TeacherGetSerializer(teacher, many=True)
                return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.RETRIEVED})
            except:
                return Response({'data': None, 'code': status.HTTP_204_NO_CONTENT, 'message': general_message.RECORD_NOT_FOUND})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})

    def update(self, request, pk, format=None):
        """Update Teacher."""
        try:
            try:
                teacher = Teacher.objects.get(id=pk)
                serializer = TeacherCreateUpdateSerializer(teacher, data=request.data, partial=True)
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
        """Delete Teacher."""
        try:
            try:
                teacher = Teacher.objects.get(id=pk)
                teacher.delete()
                return Response({'data':{}, 'code':status.HTTP_200_OK, 'message':general_message.DELETE})
            except:
                return Response({'data':None, 'code':status.HTTP_204_NO_CONTENT, 'message':general_message.RECORD_NOT_FOUND})
        except Exception as e:
            return Response({'data':None, 'code':status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})
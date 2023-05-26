from rest_framework import status
from rest_framework.response import Response
from core.models import College 
from core.serializers import CollegeSerializer
from core.utils import general_message
from .college_base_services import CollegeBaseService


class CollegeService(CollegeBaseService):
    def __init__(self):
        pass

    def create(self, request, format=None):
        """Create college."""
        try:
            serializer = CollegeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.CREATED})
            else:
                return Response({'data': None, 'code': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})

    def get(self, request, pk, format=None):
        """Get College."""
        try:
            try:
                college = College.objects.get(id=pk)
                serializer = CollegeSerializer(college)
                return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.RETRIEVED})
            except:
                return Response({'data': None, 'code': status.HTTP_204_NO_CONTENT, 'message': general_message.RECORD_NOT_FOUND})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})
        
    def get_list(self, request, format=None):
        """Get College list."""
        try:
            try:
                college = College.objects.all()
                serializer = CollegeSerializer(college, many=True)
                return Response({'data': serializer.data, 'code': status.HTTP_200_OK, 'message': general_message.RETRIEVED})
            except:
                return Response({'data': None, 'code': status.HTTP_204_NO_CONTENT, 'message': general_message.RECORD_NOT_FOUND})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})

    def update(self, request, pk, format=None):
        """Update college."""
        try:
            try:
                college = College.objects.get(id=pk)
                serializer = CollegeSerializer(college, data=request.data, partial=True)
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
        """Delete college."""
        try:
            try:
                user = College.objects.get(id=pk)
                user.delete()
                return Response({'data':{}, 'code':status.HTTP_200_OK, 'message':general_message.DELETE})
            except:
                return Response({'data':None, 'code':status.HTTP_204_NO_CONTENT, 'message':general_message.RECORD_NOT_FOUND})
        except Exception as e:
            return Response({'data':None, 'code':status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})
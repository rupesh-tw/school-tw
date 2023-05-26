from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.services import TeacherService

teacher_service = TeacherService()

@api_view(['POST'])
def teacher_create_view(request, format=None):
    # breakpoint()
    result = teacher_service.create(request, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['GET'])
def teacher_get_view(request, pk, format=None):
    result = teacher_service.get(request, pk, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['PUT'])
def teacher_update_view(request, pk=None, format=None):
    result = teacher_service.update(request, pk, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['DELETE'])
def teacher_delete_view(request, pk=None, format=None):
    result = teacher_service.delete(request, pk, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['GET'])
def teacher_list_view(request, format=None):
    result = teacher_service.get_list(request, format=None)
    return Response(result.data, status=result.data["code"])

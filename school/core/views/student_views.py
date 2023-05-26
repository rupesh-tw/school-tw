from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.services import StudentService

student_service = StudentService()

@api_view(['POST'])
def student_create_view(request, format=None):
    # breakpoint()
    result = student_service.create(request, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['GET'])
def student_get_view(request, pk, format=None):
    result = student_service.get(request, pk, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['PUT'])
def student_update_view(request, pk=None, format=None):
    result = student_service.update(request, pk, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['DELETE'])
def student_delete_view(request, pk=None, format=None):
    result = student_service.delete(request, pk, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['GET'])
def student_list_view(request, format=None):
    result = student_service.get_list(request, format=None)
    return Response(result.data, status=result.data["code"])

from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.services import CollegeService

college_service = CollegeService()


@api_view(['POST'])
def college_create_view(request, format=None):
    # breakpoint()
    result = college_service.create(request, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['GET'])
def college_get_view(request, pk=None, format=None):
    result = college_service.get(request, pk, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['PUT'])
def college_update_view(request, pk=None, format=None):
    result = college_service.update(request, pk, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['DELETE'])
def college_delete_view(request, pk=None, format=None):
    result = college_service.delete(request, pk, format=None)
    return Response(result.data, status=result.data["code"])

@api_view(['GET'])
def college_list_view(request, format=None):
    result = college_service.get_list(request, format=None)
    return Response(result.data, status=result.data["code"])
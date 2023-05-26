from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.services import StudentService


@api_view(['GET', 'POST'])
def college_create_update_view(request, format=None):
    result = StudentService.create_update(request, format=None)
    if request.method == 'POST':
        return Response(result.data, status=result.data["code"])
    return Response(result.data, status=result.data["code"])

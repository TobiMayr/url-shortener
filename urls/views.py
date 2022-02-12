from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponseRedirect
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from urls.serializers import UrlSerializer
from urls.models import Url, Visit

validate = URLValidator()


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def url_add(request):
    """
    List all code urls, or create a new url.
    """
    new_visit = Visit(url_path=request.path)
    new_visit.save()

    serializer = UrlSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        validate(request.data['originalUrl'])
    except ValidationError as exception:
        return Response(exception.message, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def url_redirect(request, pk):
    """
    Redirect to original url
    """
    new_visit = Visit(url_path=request.path)
    new_visit.save()
    try:
        url = Url.objects.get(pk=pk)
    except Url.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return HttpResponseRedirect(redirect_to=url.original_url)

from django.http import HttpResponseRedirect
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from urls.serializers import UrlSerializer
from urls.models import Url


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def url_add(request):
    """
    List all code urls, or create a new url.
    """
    serializer = UrlSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def url_redirect(request, pk):
    """
    Redirect to original url
    """
    try:
        url = Url.objects.get(pk=pk)
    except Url.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return HttpResponseRedirect(redirect_to=url.original_url)

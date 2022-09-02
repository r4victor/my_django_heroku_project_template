from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response

from core.utils.auth_utils import MyAPIKeyAuthentication
from core.utils.logging_utils import get_logger


logger = get_logger(__name__)


@api_view(['GET'])
@authentication_classes([MyAPIKeyAuthentication])
def endpoint(request: Request) -> Response:
    logger.info(f'Processing request...')
    data = {
        'data': 'Hello!'
    }
    return Response(data)

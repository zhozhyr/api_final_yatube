from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and 'detail' in response.data:
        if response.data['detail'] == 'Token is invalid':
            response.data['detail'] = 'Token is invalid or expired'

    return response

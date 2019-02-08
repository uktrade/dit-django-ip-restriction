from django.conf import settings
from django.http import HttpResponse
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

from basicauth.basicauthutils import validate_request
from basicauth.response import HttpResponseUnauthorized

from .ip_filter import is_valid_ip, is_valid_admin_ip, get_client_ip


class IpRestrictionOrBasicAuth(MiddlewareMixin):
    """Verify the client's IP and revert to basic auth if the IP is not white listed"""
    def process_request(self, request):
        if settings.ENABLE_IP_SAFELIST:
            client_ip = get_client_ip(request)

            if not is_valid_ip(client_ip):
                if not validate_request(request):
                    return HttpResponseUnauthorized()

        return None


# def IpRestrictionOrBasicAuth(get_response):
#     """Verify the client's IP and revert to basic auth if the IP is not white listed"""
#
#     def middleware(request):
#         if settings.ENABLE_IP_SAFELIST:
#             client_ip = get_client_ip(request)
#
#             if not is_valid_ip(client_ip):
#                 if not validate_request(request):
#                     return HttpResponseUnauthorized()
#
#         return get_response(request)
#
#     return middleware


def IpRestriction(get_response):
    """Verify the client's IP"""

    def middleware(request):
        if settings.ENABLE_IP_SAFELIST:
            client_ip = get_client_ip(request)

            if not is_valid_ip(client_ip):
                if not validate_request(request):
                    return HttpResponseUnauthorized()

        return get_response(request)

    return middleware


def AdminIpRestrictionMiddleware(get_response):
    """Apply IP white listing to the admin only"""

    def middleware(request):
        if resolve(request.path).app_name == 'admin':
            if settings.ENABLE_ADMIN_IP_SAFELIST:
                client_ip = get_client_ip(request)

                if not is_valid_admin_ip(client_ip):
                    return HttpResponse('Unauthorized', status=401)

        return get_response(request)

    return middleware

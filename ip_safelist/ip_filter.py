from ipaddress import ip_network, ip_address
import logging

from django.conf import settings

logger = logging.getLogger(__file__)


XFF_IP_INDEX = getattr(settings, 'IP_SAFELIST_XFF_IP_INDEX', -3)


def is_valid_admin_ip(client_ip):

    if not client_ip:
        return False

    if client_ip in settings.ALLOWED_ADMIN_IPS:
        return True

    ip_addr = ip_address(client_ip)
    for cidr in settings.ALLOWED_ADMIN_IP_RANGES:
        if ip_addr in ip_network(cidr):
            return True

    return False


def is_valid_ip(client_ip):

    if not client_ip:
        return False

    if client_ip in settings.ALLOWED_IPS:
        return True

    ip_addr = ip_address(client_ip)
    for cidr in settings.ALLOWED_IP_RANGES:
        if ip_addr in ip_network(cidr):
            return True

    return False


def get_client_ip(request):

    try:
        return request.META['HTTP_X_FORWARDED_FOR'].split(',')[XFF_IP_INDEX].strip()
    except (IndexError, KeyError):
        logger.warning(
            'X-Forwarded-For header is missing or does not '
            'contain enough elements to determine the '
            'client\'s ip')
        return None

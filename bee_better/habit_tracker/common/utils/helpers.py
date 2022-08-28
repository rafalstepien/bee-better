from datetime import datetime
from django.core.handlers.wsgi import WSGIRequest


def is_ajax(request: WSGIRequest) -> bool:
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def _date_from_slash_to_dash(date: str) -> str:
    """
    Converts date from DD/MM/YYYY format to YYYY-MM-DD format.
    """
    return datetime.strptime(date, '%d/%m/%Y').strftime("%Y-%m-%d")

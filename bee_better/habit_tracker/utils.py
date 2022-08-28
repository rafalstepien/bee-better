from django.core.handlers.wsgi import WSGIRequest


def is_ajax(request: WSGIRequest) -> bool:
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"

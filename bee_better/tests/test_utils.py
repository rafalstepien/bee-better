import pytest
from habit_tracker.common.utils.helpers import is_ajax
from unittest.mock import Mock

@pytest.mark.parametrize(
    "meta, expected_return",
    [
        ({"HTTP_X_REQUESTED_WITH": ""}, False),
        ({"HTTP_X_REQUESTED_WITH": "somemeta"}, False),
        ({"HTTP_X_REQUESTED_WITH": None}, False),
        ({"HTTP_X_REQUESTED_WITH": "XMLHttpRequest"}, True),
    ]
)
def test_is_ajax(meta, expected_return):
    mock_wsgi_request = Mock(
        META=meta
    )
    assert is_ajax(mock_wsgi_request) == expected_return

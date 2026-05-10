__all__ = [
    "DataGoKrError",
    "APIKeyError",
    "RateLimitError",
    "APIResponseError",
    "InvalidParameterError",
    "MissingParameterError",
    "NoDataFoundError",
    "ServerSideError",
    "NetworkError",
]


class DataGoKrError(Exception):
    """Base exception for 공공데이터포털 OpenAPI client."""


class APIKeyError(DataGoKrError):
    """Invalid or missing API key."""


class RateLimitError(DataGoKrError):
    """Daily traffic limit exceeded."""


class APIResponseError(DataGoKrError):
    """Generic API error response."""


class InvalidParameterError(APIResponseError):
    """Invalid parameter value."""


class MissingParameterError(APIResponseError):
    """Required parameter missing."""


class NoDataFoundError(DataGoKrError):
    """No data found for the query."""


class ServerSideError(DataGoKrError):
    """Server-side error."""


class NetworkError(DataGoKrError):
    """Network or connection error."""

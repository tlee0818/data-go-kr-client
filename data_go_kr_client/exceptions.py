__all__ = [
    "DataGoKrClientError",
    "APIKeyError",
    "RateLimitError",
    "APIResponseError",
    "InvalidParameterError",
    "MissingParameterError",
    "NoDataFoundError",
    "ServerSideError",
    "NetworkError",
]


class DataGoKrClientError(Exception):
    """Base exception for 공공데이터포털 OpenAPI client."""


class APIKeyError(DataGoKrClientError):
    """Invalid or missing API key."""


class RateLimitError(DataGoKrClientError):
    """Daily traffic limit exceeded."""


class APIResponseError(DataGoKrClientError):
    """Generic API error response."""


class InvalidParameterError(APIResponseError):
    """Invalid parameter value."""


class MissingParameterError(APIResponseError):
    """Required parameter missing."""


class NoDataFoundError(DataGoKrClientError):
    """No data found for the query."""


class ServerSideError(DataGoKrClientError):
    """Server-side error."""


class NetworkError(DataGoKrClientError):
    """Network or connection error."""

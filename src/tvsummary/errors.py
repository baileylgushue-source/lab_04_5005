class TVSummaryError(Exception):
    """Base error for the TV summary package."""


class DataError(TVSummaryError):
    """Raised when TV show data is invalid."""


class SettingsError(TVSummaryError):
    """Raised when configuration settings are invalid."""


class SourceError(TVSummaryError):
    """Raised when TV show data cannot be retrieved."""
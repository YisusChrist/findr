"""Constants for the project."""

try:
    from importlib import metadata
except ImportError:  # for Python < 3.8
    import importlib_metadata as metadata  # type: ignore

__version__: str = metadata.version(__package__ or __name__)
__desc__: str = metadata.metadata(__package__ or __name__)["Summary"]
PACKAGE: str = metadata.metadata(__package__ or __name__)["Name"]
GITHUB: str = metadata.metadata(__package__ or __name__)["Home-page"]

HIGHLIGHT_MAX_LEN = 40

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

DEBUG = False
PROFILE = False

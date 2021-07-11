# type: ignore[attr-defined]
"""In which I rework my old discord bot to be better, faster, more efficient, and have better commands."""

try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:  # pragma: no cover
    from importlib_metadata import PackageNotFoundError, version


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "v0.9.5"
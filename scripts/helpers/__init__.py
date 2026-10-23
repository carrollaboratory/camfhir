import logging
import sys
from pathlib import Path
from typing import Any

from glom import glom
from yaml import safe_load

# Rich Logging if rich is installed
if sys.stderr.isatty():
    from rich.console import Console
    from rich.logging import RichHandler
    from rich.traceback import install


class Config:
    config_filename = Path.cwd() / "config/dev.yaml"
    _config: dict[str, Any] = {}

    @classmethod
    def configuration(cls) -> dict[str, Any]:
        if not cls._config:
            cls._config = safe_load(cls.config_filename.open("r", encoding="utf-8"))

        return cls._config

    @classmethod
    def value_for(cls, key: str, default: Any = "") -> Any:
        """Supports dot notation for nested keys like 'test-profiles.debug.url'"""
        return glom(cls.configuration, key, default=default)


def init_logging(loglevel: str | None = None):
    # When we are in the terminal, let's use the rich logging
    if loglevel is None:
        loglevel = "WARN"
    DATEFMT = "%Y-%m-%dT%H:%M:%SZ"
    if sys.stderr.isatty():
        install(show_locals=True)

        handler = RichHandler(
            level=loglevel,
            console=Console(stderr=True),
            show_time=False,
            show_level=True,
            markup=True,
            rich_tracebacks=True,
        )
        FORMAT = "%(message)s"
    else:
        FORMAT = "%(asctime)s\t%(levelname)s\t%(message)s"
        handler = logging.StreamHandler()

    logging.basicConfig(
        level=loglevel, format=FORMAT, datefmt=DATEFMT, handlers=[handler]
    )
